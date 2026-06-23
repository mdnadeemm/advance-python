class InMemoryDB:
    def __init__(self):
        self.records = {}
        self.mod_count = {}
        self.locks = {}  # {keys: user_id}

    def set_or_inc(self, key: str, field: str, value: int) -> int | None:

        if key not in self.records:
            self.records[key] = {}
        if field not in self.records[key]:
            self.records[key][field] = value
        else:
            self.records[key][field] += value
        self.mod_count[key] = self.mod_count.get(key, 0) + 1
        return self.records[key][field]

    def get(self, key: str, field: str) -> int | None:

        if key not in self.records or field not in self.records[key]:
            return None

        return self.records[key][field]

    def delete(self, key: str, field: str) -> bool:

        if key not in self.records:
            return False

        if field in self.records[key]:
            del self.records[key][field]
            self.mod_count[key] += 1
            if len(self.records[key]) <= 0:
                del self.records[key]
                del self.mod_count[key]

            return True

        return False

    def top_n_keys(self, n: int) -> list[str]:
        top_n = sorted(self.mod_count.items(), key=lambda item: (-item[1], item[0]))[:n]

        top_n_str = []

        for key, mod in top_n:
            top_n_str.append(f"{key}({mod})")

        return top_n_str

    def lock(self, user_id: str, key: str) -> str | None:
        if key not in self.records:
            return "invalid_request"
        if key not in self.locks:
            self.locks[key] = user_id
            return "acquired"

        if self.locks[key] == user_id:
            return None

        if self.locks[key] != user_id:
            return "wait"

    def unlock(self, key: str) -> str | None:
        if key not in self.records:
            return "invalid_request"
        if key not in self.locks:
            return None
        else:
            del self.locks[key]
            return "released"

    def set_or_inc_by_user(
        self, key: str, field: str, value: int, user_id: str
    ) -> int | None:
        if key not in self.records:
            self.records[key] = {}

        if key not in self.locks or (key in self.locks and self.locks[key] == user_id):
            if field not in self.records[key]:
                self.records[key][field] = value

                return self.records[key][field]

            else:
                if key in self.locks and self.locks[key] == user_id:
                    self.records[key][field] += value
                else:
                    return self.records[key][field]

        if key in self.locks and self.locks[key] == user_id:
            self.mod_count[key] = self.mod_count.get(key, 0) + 1

        return self.records[key][field]

    def delete_by_user(self, key: str, field: str, user_id: str) -> bool:

        if key not in self.records:
            return False

        if (
            key in self.locks
            and field in self.records[key]
            and self.locks[key] == user_id
        ):
            del self.records[key][field]
            self.mod_count[key] += 1
            if len(self.records[key]) <= 0:
                del self.records[key]
                del self.mod_count[key]
                del self.locks[key]

            return True

        return False


def test_level_1():
    print("Running Level 1 Tests...")
    db = InMemoryDB()

    # 1. Basic insertion
    assert db.set_or_inc("record_A", "field_1", 10) == 10

    # 2. Incrementing an existing field
    assert db.set_or_inc("record_A", "field_1", 5) == 15

    # 3. Adding a second field to the same record
    assert db.set_or_inc("record_A", "field_2", 20) == 20

    # 4. Getting values
    assert db.get("record_A", "field_1") == 15

    # 5. Getting a non-existent field or record
    assert db.get("record_A", "field_3") is None
    assert db.get("record_B", "field_1") is None

    # ADD THIS PRINT STATEMENT HERE:
    print("Current Database State:", db.records)

    # 6. Deleting a field
    assert db.delete("record_A", "field_2") is True
    assert db.get("record_A", "field_2") is None

    # 7. Deleting a non-existent field
    assert db.delete("record_A", "field_3") is False

    # 8. Deleting the last field should delete the entire record
    assert db.delete("record_A", "field_1") is True
    assert "record_A" not in db.records  # Verifies the empty record was removed

    print("Level 1 Tests Passed! ✅")


# Run the test
test_level_1()


def test_level_2():
    print("\nRunning Level 2 Tests...")
    db = InMemoryDB()

    # 1. Populate the database and rack up modification counts
    # user_A will have 3 modifications
    db.set_or_inc("user_A", "gold", 10)
    db.set_or_inc("user_A", "gold", 5)
    db.set_or_inc("user_A", "silver", 2)

    # user_B will have 2 modifications
    db.set_or_inc("user_B", "gold", 50)
    db.set_or_inc("user_B", "gold", 10)

    # user_C will have 2 modifications
    db.set_or_inc("user_C", "gold", 100)
    db.set_or_inc("user_C", "gold", 0)  # Increasing by 0 still counts as a mod!

    # 2. Test top_n_keys sorting and tie-breakers
    # Expected order: A (3 mods), then B (2 mods), then C (2 mods)
    # B and C are tied, so they sort alphabetically: "user_B" comes before "user_C"
    expected_top_3 = ["user_A(3)", "user_B(2)", "user_C(2)"]
    assert db.top_n_keys(3) == expected_top_3

    # 3. Test returning fewer than the total number of records
    assert db.top_n_keys(2) == ["user_A(3)", "user_B(2)"]

    # 4. Test returning more 'n' than existing records
    assert db.top_n_keys(10) == expected_top_3

    # 5. Test deletion logic with top_n_keys
    # Deleting a field counts as a modification
    db.delete("user_B", "gold")
    db.delete("ho", "goe")
    # user_B's gold field was the only field. The record is now empty.
    # Level 2 rule: If a record is deleted, its mod counter MUST be deleted.

    expected_after_delete = [
        "user_A(3)",
        "user_C(2)",
    ]  # user_B should be completely gone
    assert db.top_n_keys(5) == expected_after_delete

    print("Level 2 Tests Passed! ✅")


# Run the test
test_level_2()

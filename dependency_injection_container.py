class ServiceLogger:
    def __enter__(self):
        print("Resolving Databases...")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resolved Database.")


class Container:
    _container = {}
    _instances = {}

    def resolve(self, name):

        # Return existing singleton if available
        if name in self.__class__._instances:
            return self.__class__._instances[name]

        cls = self.__class__._container.get(name)

        if cls is None:
            raise ValueError(f"{name} not registered")

        # Manual dependency injection
        if name == "Database":
            obj = cls()

        elif name == "UserRepository":
            db = self.resolve("Database")
            obj = cls(db)

        else:
            obj = cls()

        # Save singleton instance
        self.__class__._instances[name] = obj

        return obj


def service(cls):
    Container._container.update({cls.__name__: cls})
    return cls


@service
class Database:
    pass


@service
class UserRepository:
    def __init__(self, db):
        self.db = db


container = Container()
with ServiceLogger():
    db1 = container.resolve("Database")
    db2 = container.resolve("Database")

    print(db1)
    print(db2)

    print("db1 is db2:", db1 is db2)

    repo1 = container.resolve("UserRepository")
    repo2 = container.resolve("UserRepository")

    print(repo1)
    print(repo2)

    print("repo1 is repo2:", repo1 is repo2)

    print("repo1.db is db1:", repo1.db is db1)

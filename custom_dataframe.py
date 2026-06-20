class DataFrame:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"DataFrame({self.data})"

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __iter__(self):
        return iter(self.data)


df = DataFrame([{"name": "Nadeem", "age": 22}, {"name": "Ali", "age": 20}])

print(df)
print(len(df))
print(df[0])

for row in df:
    print(row)

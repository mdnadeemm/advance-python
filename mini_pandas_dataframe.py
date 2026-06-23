class DataFrame:
    def __init__(self, data):
        self.data = data
        self.count = 0

    def __repr__(self):

        rows = []

        rows.append(" ".join(self.data[0].keys()))

        for value in self.data:
            rows.append(" ".join(map(str, value.values())))

        return "\n".join(rows)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        column = []
        for item in self.data:
            column.append(item.get(key))

        return column

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):

        if self.count >= len(self.data):
            raise StopIteration

        result = self.data[self.count]

        self.count += 1

        return result

    def filter(self, age):

        for item in self.data:
            if item.get("age") == age:
                yield item

    def select(self, *args):
        data = []

        for item in self.data:
            data_item = {}
            for arg in args:
                data_item.update({arg: item.get(arg)})
            data.append(data_item)

        return data

    def first(self):
        return self.data[0]

    def last(self):
        return self.data[-1]

    def sort(self, sortby):
        return sorted(self.data, key=lambda item: item.get(sortby))


df = DataFrame(
    [
        {"name": "Nadeem", "age": 22},
        {"name": "Ali", "age": 20},
        {"name": "Ahmed", "age": 22},
    ]
)

print(df)
print(df["age"])
for row in df:
    print(row)
for row in df:
    print(row)

for row in df.filter(age=22):
    print(row)
print(df.select("name"))
print(df.select("name", "age"))
print(df.first())
print(df.last())
print(df.sort("age"))

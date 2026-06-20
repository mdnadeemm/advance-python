class OwnGen:
    def __init__(self, n):
        self.count = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration

        value = self.count

        self.count += 1

        return value


for i in OwnGen(5):
    print(i)

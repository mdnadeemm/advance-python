class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > self.n:
            raise StopIteration
        return self.current


for x in EvenNumbers(10):
    print(x)

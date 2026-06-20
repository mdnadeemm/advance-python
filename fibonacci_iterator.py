class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.previous = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.previous > self.n:
            raise StopIteration
        result = self.previous
        self.previous, self.current = self.current, self.previous + self.current
        return result


for x in Fibonacci(20):
    print(x)

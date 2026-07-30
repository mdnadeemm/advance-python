class CounterIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration

        result = self.current
        self.current += 1
        return result




class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end


    def __iter__(self):
        return CounterIterator(self.current, self.end)



obj = Counter(1,5)
for i in obj:
    print(i)
obj = Counter(1,5)
for i in obj:
    print(i)

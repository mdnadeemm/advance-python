import time


class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()
        elapsed = self.end - self.start
        print(f"Execution time: {elapsed}")


def counter(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        result = func(*args, **kwargs)
        print(f"Function called {count} times")

        return result

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        with Timer():
            result = func(*args, **kwargs)
        return result

    return wrapper


@counter
@timer
def add(a, b):
    return a + b


print(add(10, 20))
print(add(30, 40))

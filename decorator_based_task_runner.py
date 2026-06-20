import time
from functools import wraps


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

    @wraps(func)
    def wrapper():
        nonlocal count
        count += 1
        func()
        print(f"Functino called {count} times")

    return wrapper


def timer(func):
    @wraps(func)
    def wrapper():
        with Timer():
            func()

    return wrapper


@timer
@counter
def process():
    pass


process()
process()

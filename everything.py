import time
from functools import wraps


class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()
        elapsed = self.end - self.start
        print(f"Execution time {elapsed}")


def counter(func):
    count = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        result = func(*args, **kwargs)
        print(f"Function called {count} times")
        return result

    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with Timer():
            result = func(*args, **kwargs)

        return result

    return wrapper


@counter
@timer
def fibonacci(n):

    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


print(fibonacci(10))
print(fibonacci(20))

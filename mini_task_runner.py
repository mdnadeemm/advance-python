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

    def wrapper():
        nonlocal count
        count += 1
        func()
        print(f"Function called {count} times")

    return wrapper


def timer(func):

    def wrapper():
        with Timer():
            func()

    return wrapper


@counter
@timer
def download():
    print("Downloading...")


download()
download()

import time


class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_vale, traceback):
        self.end = time.time()
        elapsed = self.end - self.start
        print(f"Execution time: {elapsed}")


def timer(func):
    def wrapper(*args, **kwargs):
        with Timer():
            func(*args, **kwargs)

    return wrapper


@timer
def hello():
    for i in range(100000):
        pass


hello()

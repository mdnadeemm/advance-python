import time


class Timer:
    def __enter__(self):

        self.start = time.time()
        print("Started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()
        elapsed = self.end - self.start
        print(f"Finished in {elapsed} seconds")


with Timer():
    for i in range(1, 10000):
        pass

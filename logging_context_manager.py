import time


class Logger:
    def __enter__(self):
        self.start = time.time()
        print("Started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()
        elapsed = self.end - self.start
        print(f"Execution time {elapsed}")
        print("Finished")


with Logger():
    print("Hello")
    print("World")

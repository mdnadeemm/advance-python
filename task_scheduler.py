class TaskRunner:
    def __enter__(self):
        print("Running ")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("done")


class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, func):
        self.tasks.append(func)

    def run(self):
        while self.tasks:
            task = self.tasks.pop(0)
            with TaskRunner():
                task()


scheduler = Scheduler()


def schedule(func):
    scheduler.add_task(func)

    return func


@schedule
def task1():
    print("Downloading file")


@schedule
def task2():
    print("Sending email")


scheduler.run()

class EventLoop:
    def __init__(self):
        self.tasks = []

    def create_task(self, func):
        self.tasks.append(func)

    def run(self):
        while self.tasks:
            task = self.tasks.pop(0)
            try:
                next(task)
                self.tasks.append(task)
            except StopIteration:
                pass


def task1():
    print("Hello")
    yield
    print("World")


def task2():
    print("I")
    yield
    print("am")


loop = EventLoop()

loop.create_task(task1())
loop.create_task(task2())

loop.run()

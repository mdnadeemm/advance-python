from functools import wraps


class Logger:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        print(f"Running {self.obj.__name__}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Finished {self.obj.__name__}")


class CLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, command):
        self.commands.update({command.__name__: command})

    def run(self, *args):

        command, arguments = args[0], args[1:]
        if command in self.commands:
            self.commands.get(command)(*arguments)
        else:
            print("command not found")


cli = CLI()


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with Logger(func):
            return func(*args, **kwargs)

    return wrapper


def command(func):
    cli.add_command(func)
    return func


@command
@logger
def hello():
    print("Hello")


@command
@logger
def bye():
    print("Bye")


@command
def greet(name):
    print(f"Hello {name}")


cli.run("bye")


@command
def add(a, b):
    print(a + b)


cli.run("add", 10, 20)
cli.run("sub", 50, 10)

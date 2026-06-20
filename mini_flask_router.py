from types import GeneratorType


class App:
    def __init__(self):
        self.routes = {}

    def add_route(self, path, page):

        self.routes.update({path: page})

    def visit(self, *args):

        path, arg = args[0], args[1:]

        func = self.routes.get(path)

        result = func(*arg)

        if isinstance(result, GeneratorType):
            while True:
                try:
                    next(result)
                except StopIteration:
                    break


app = App()


class Logger:
    def __enter__(self):
        print("Visiting /")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Finished /")


def route(path):
    def decorator(func):

        app.add_route(path, func)

        return func

    return decorator


def logger(func):
    def wrapper(*arg, **kwargs):
        with Logger():
            return func(*arg, **kwargs)

    return wrapper


@route("/")
@logger
def home():
    print("Home Page")


@route("/about")
@logger
def about():
    print("About Page")


@route("/user")
@logger
def user(name):
    print(name)


@route("/gen")
@logger
def gen():

    print("A")
    yield

    print("B")


app.visit("/about")
app.visit("/user", "Nadeem")
app.visit("/gen")

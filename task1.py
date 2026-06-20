def counter(func):

    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1

        func()
        print(f"Function called {count} times")

    return wrapper


@counter
def hello():
    print("Hello")


hello()
hello()
hello()

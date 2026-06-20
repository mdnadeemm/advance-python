def make_counter():
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        return count

    return wrapper


counter = make_counter()

print(counter())
print(counter())
print(counter())

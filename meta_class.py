class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print("1. __new__")
        return super().__new__(cls, name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        print("2. __call__")
        return super().__call__(*args, **kwargs)

class Student(metaclass=MyMeta):
    def __new__(cls):
        print("3. Student __new__")
        return super().__new__(cls)

    def __init__(self):
        print("4. Student __init__")

print("-----")
s = Student()

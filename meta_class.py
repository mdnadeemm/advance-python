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




class MasterMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        print(f"1. __prepare__ for {name}")
        return dict()  # Returns the namespace storage

    def __new__(cls, name, bases, namespace, **kwargs):
        print(f"2. __new__ for {name}")
        return super().__new__(cls, name, bases, namespace)

    def __init__(cls, name, bases, namespace, **kwargs):
        print(f"3. __init__ for {name}")
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        print(f"4. __call__ to create instance of {cls.__name__}")
        return super().__call__(*args, **kwargs)

# --- This triggers steps 1, 2, and 3 ---
print("--- Defining Class ---")
class Product(metaclass=MasterMeta):
    pass

# --- This triggers step 4 ---
print("\n--- Creating Instance ---")
item = Product()

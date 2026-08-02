class Student:

    # it is called when attribute is present
    def __getattribute__(self, name):
        print(f"Looking for {name}")
        return super().__getattribute__(name)

    def __init__(self):
        self.age = 20

s = Student()
print(s.age)            # Python does obj.__getattribute__("name")

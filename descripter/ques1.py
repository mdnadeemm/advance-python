class Positive:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(f"{self.name} must be positive")
        obj.__dict__[self.name] = value

    def __get__(self, obj, objtype):
        if self.name not in obj.__dict__:
            raise AttributeError(f"{self.name} has not been set")
        return obj.__dict__[self.name]



class Student:
    age = Positive()
    marks = Positive()
    salary = Positive()
s = Student()
print(s.age)
s.age = 25
print(s.age)
s.marks = -15
s.age = -10    # ValueError("Age must be positive")

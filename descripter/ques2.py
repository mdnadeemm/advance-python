"""Create a descriptor called Typed."""
class Typed:
    def __init__(self, ourtype):
        self.ourtype = ourtype

    def __set_name__(self, owner, name):
        self.name = name
    def __set__(self, obj, value):
        if not isinstance(value,self.ourtype):
            raise TypeError(f"{self.name} should be {self.ourtype} type")
        obj.__dict__[self.name] = value

    def __get__(self, obj, objtype):
        if obj is None:
            return self
        if self.name not in obj.__dict__:
            raise AttributeError(f"{self.name} is not set")
        return obj.__dict__[self.name]

class Student:
    age = Typed(int)
    name = Typed(str)
    marks = Typed(float)



s = Student()

s.age = 20          # ✅
s.name = "Nadeem"   # ✅
s.marks = 95.5      # ✅
print(Student.age)

s.age = "20"        # ❌ TypeError
s.name = 100        # ❌ TypeError
s.marks = "90.5"    # ❌ TypeError

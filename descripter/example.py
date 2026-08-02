class Positive:

    def __get__(self, obj, objtype):
        return obj.__dict__["age"]

    def __set__(self, obj, value):

        if value < 0:
            raise ValueError("Age cannot be negative")

        obj.__dict__["age"] = value


class Student:

    age = Positive()


s=Student()
s.age = 25
s.age = -12

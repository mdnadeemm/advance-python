"""
What is a Descriptor?

A descriptor is simply an object that defines one or more of these methods:
__get__()
__set__()
__delete__()
"""

class MyDescripter:

    def __set__(self, obj, value):
            print("Setting", value)

    def __get__(self, obj, objtype):
        print("GET")
        return 100

    def __delete__(self, obj):
            print("Deleted")


class Student:
    age = MyDescripter()

s = Student()
print(s.age)

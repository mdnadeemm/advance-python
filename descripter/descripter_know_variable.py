class Positive:
    def __set_name__(self, owner, name):
        self.name = name

class Student:
    age = Positive()
    height = Positive()

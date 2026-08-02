""" this MyMethod should be implemented to show bound method """
class MyMethod:
    def __init__(self, func, sobj):
        self.func = func
        self.sobj = sobj

    def __call__(self, *args , **kwargs):
        return self.func(self.sobj, *args, **kwargs)




def hello(self):
    print("Hello", self.name)

class Student:
    def __init__(self):
        self.name = "Nadeem"

    def add(self, a, b):
        print(self.name, a+b)

s = Student()

m = MyMethod(hello, s)

m()
m = MyMethod(Student.add, s)
m(1,2)

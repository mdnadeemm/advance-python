class Student:
    def __getattribute__(self, name):
        return self.name                       # self again call __getattribute__ so infinite recursion
                                               # use return super().__getattribute__(name) inside and never self.name

    def __init__(self):
        self.name = 4
s = Student()
print(s.name)

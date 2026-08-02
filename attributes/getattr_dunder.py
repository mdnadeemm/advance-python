class Student:

    # it is called when attribute is not found by __getattribute__
    def __getattr__(self, name):
        print("Not Found")
        return "Default"


s = Student()

print(s.xyz)   # xyz is not present so it call obj.__getattr__(name)

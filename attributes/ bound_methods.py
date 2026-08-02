"""
Class access
Student.hello
        │
        ▼
Function Object




Instance access
s.hello
     │
     ▼
function.__get__(s, Student)
     │
     ▼
Bound Method
     │
     ▼
Stores

Function
Instance
"""

class Student:

    def hello(self):
        pass

s = Student()

m = s.hello

# both calling is same
calling_s = s.hello() # it automatically recieve self from bound method
calling_s_1  =  Student.hello(s) # manually passing self

print(m.__self__)
print(m.__func__)

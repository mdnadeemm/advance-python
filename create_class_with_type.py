def greet(self):
    print("hello")

Student = type(
    "Student",
    (),
    {
        "x": 10,
        "greet": greet
    }
)

s = Student()
print(s.x)
s.greet()

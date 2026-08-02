class Student:
    def __getattribute__(self, name):
        print(f"Accessing {name}")
        return super().__getattribute__(name)    # attribute not found it raises AttributeError



    def __getattr__(self, name):                 # python catches AttributeError and call __getattr__
        """ __getattr__ called when __getattribute__ raises AttributeError """
        return f"{name} does not exit"
    def __init__(self):
        self.name = "Nadeem"

s = Student()

"""
Output
Accessing name
Nadeem
"""
print(s.name)

"""
Accessing age
age does not exist
"""

print(s.age)

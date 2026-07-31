Animal = type(
    "Animal",
    (),
    {
        "sound": lambda self: print("sound")
    }
)

#inherit Animal class

Dog = type(
    "Dog",
    (Animal,),
    {

    }
)
s = Dog()

s.sound()

def name(self,name):
    super(type(self),self).name(name)

Fru = type(
    "Fruit",
    (),
    {
        "name": lambda self,name: print(name)
    }
)

Mango = type(
    "Mango",
    (Fru,),
    {
        "name": name
    }
)

m = Mango()
m.name("mango")


#---------------------------------------------

def init(self, name):
    self.name = name
def new(cls, *args, **kwargs):
    print("creating student")
    return super(Student, cls).__new__(cls)
def call(self):
    print("I am callable")
Student = type(
    "Student",
    (),
    {
        "__init__": init,
        "__new__": new,
        "__call__": call


    }
)

s = Student("Nadeem")
s()

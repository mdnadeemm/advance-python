class Model:
    def save(self):
        print(f"Saving {self}")


class IntegerField:
    def __get__(self, obj, owner):
        return obj._age

    def __set__(self, obj, value):
        obj._age = value


class User(Model):
    age = IntegerField()

    def __init__(self, **kwargs):
        self.user = kwargs

    def __repr__(self):
        return f"User({self.user}"

    def __setattr__(self, name, value):
        print(f"Field name changed from {self.__dict__.get(name)} to {value}")
        super().__setattr__(name, value)


user = User(name="Nadeem", age=22)
user.age = 65
print(user)
user.save()

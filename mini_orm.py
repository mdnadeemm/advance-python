class Model:
    def save(self):
        print("saving to database..........")
        print(self.__dict__)


class IntegerField:
    def __get__(self, obj, owner):
        return obj._age

    def __set__(self, obj, value):
        obj._age = value


class StringField:
    def __get__(self, obj, owner):
        return obj._name

    def __set__(self, obj, value):
        obj._name = value


class User(Model):
    name = StringField()
    age = IntegerField()


u = User()
u.name = "Nadeem"
u.age = 22

print(u.name, u.age)
u.save()

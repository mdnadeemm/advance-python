"""build a mini Django ORM."""
class Field:
    expected_type = object
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, obj, value):

        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.name} should be {self.expected_type.__name__} type")
        obj.__dict__[self.name] = value

    def __get__(self, obj, objtype):
        if obj is None:
            return self

        if self.name not in obj.__dict__:
            raise AttributeError(f"{self.name} is not set")

        return obj.__dict__[self.name]

class IntegerField(Field):
    expected_type = int

class CharField(Field):
    expected_type = str


class MyMeta(type):
    def __new__(cls, name, bases, namespace, **kwargs):

        def to_dict(self):
            fields = {}
            for key in self._fields:

                fields[key] = getattr(self, key)
            return fields

        print(f"Creating {name} \nFields:")
        field = {}
        for key, value in namespace.items():
            if isinstance(value, Field):
                field[key] = value
                print(key)
        namespace["_fields"] = field
        namespace["to_dict"] = to_dict

        return super().__new__(cls, name, bases, namespace, **kwargs)

"""
setattr used because it follow descripter
and got to the descripter __set__ or __get__
but instance.__dict__[key] = value directly change
the value without validation

Remember this rule
setattr()
Triggers descriptors
Triggers properties
Triggers __setattr__

__dict__
Direct memory write

No validation

No descriptor

No property
"""

class Model(metaclass=MyMeta):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class User(Model):
    id = IntegerField()
    name = CharField()

u = User()

u.id = 10
u.name = "Nadeem"

print(u.id)      # 10
print(u.name)    # Nadeem
print(User._fields)
print(u.to_dict())
uv = User(id=12,name="uber")
print(uv.id)
print(uv.to_dict())


#u.id = "10"      # TypeError
#u.name = 100     # TypeError

class Model:
    registry = []

    def __init_subclass__(cls):
        Model.registry.append(cls)
        cls._records = []

    def save(self):
        self.__class__._records.append(self)

    @classmethod
    def all(cls):
        return cls._records


class User(Model):
    pass


class Product(Model):
    pass


print(Model.registry)

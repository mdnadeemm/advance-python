class Model:
    registry = []

    def __init_subclass__(cls):
        Model.registry.append(cls)
        print(f"Registered class {cls.__name__}")


class User(Model):
    def __repr__(self):
        return "User"


class Product(Model):
    def __repr__(self):
        return "Product()"


print(Model.registry)

class ConfigLogger:
    def __enter__(self):
        print("Saving configuration...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Saved.")


class Config:
    _records = []

    @classmethod
    def all(cls):
        return cls._records


class StringField:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError

        obj.__dict__[self.name] = value


class IntegerField:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError
        obj.__dict__[self.name] = value


registry = []


def register_config(cls):
    registry.append(cls)
    return cls


@register_config
class AppConfig(Config):
    host = StringField()
    port = IntegerField()

    def save(self):

        print("saving.......")

        self.__class__._records.append(self)

    def __setattr__(self, name, value):
        print(f"Field {name} changed from {self.__dict__.get(name)} to {value}")
        super().__setattr__(name, value)

    def __repr__(self):
        return f"AppConfig(host={self.__dict__.get('host')},port={self.__dict__.get('port')})"


config = AppConfig()
config.host = "localhost"
config.port = 8000
print(config)

config.host = "googl.com"
config.port = 20554
with ConfigLogger():
    config.save()

print(AppConfig.all())

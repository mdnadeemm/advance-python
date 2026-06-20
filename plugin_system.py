class PluginRunner:
    def __init__(self, plugin):
        self.plugin = plugin

    def __enter__(self):
        print(f"Starting {self.plugin.__name__}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Finished {self.plugin.__name__}")


class PluginManager:
    def __init__(self):
        self.plugins = []

    def add_plugin(self, plugin):
        self.plugins.append(plugin)

    def run_all(self):
        while self.plugins:
            plugin = self.plugins.pop(0)
            with PluginRunner(plugin):
                plugin()


manager = PluginManager()


def register(func):
    manager.add_plugin(func)
    return func


@register
def plugin_a():
    print("Plugin A")


@register
def plugin_b():
    print("Plugin B")


manager.run_all()

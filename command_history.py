class CommandHistory:
    _command_history = []

    def __call__(self, command):
        self.__class__._command_history.append(command)

    def show(self):
        for index, item in enumerate(self.__class__._command_history):
            print(f"{index + 1}. {item}")


history = CommandHistory()
history("ls")
history("cd projects")
history("python app.py")

history.show()

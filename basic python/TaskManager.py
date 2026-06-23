class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        return self.tasks

    def delete_tasks(self, task):
        self.tasks.remove(task)


task_manager = TaskManager()

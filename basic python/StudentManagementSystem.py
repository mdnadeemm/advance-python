class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_students(self, student):
        self.students.append(student)

    def show_students(self):
        return self.students

    def search_student(self, name):
        for student in self.students:
            if student.get("name") == name:
                return student

    def delete_student(self, name):
        for student in self.students:
            if student.get("name") == name:
                self.students.remove(student)


sms = StudentManagementSystem()
sms.add_students({"name": "Nadeem", "age": 22, "marks": 83})
sms.add_students({"name": "Danish", "age": 21, "marks": 81})
sms.add_students({"name": "Abdul", "age": 23, "marks": 82})
sms.add_students({"name": "Osama", "age": 27, "marks": 87})
sms.add_students({"name": "Omama", "age": 29, "marks": 89})
print(sms.search_student("Abdul"))
sms.delete_student("Abdul")
print(sms.search_student("Abdul"))

print(sms.show_students())

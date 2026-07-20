@dataclass
class Student:
    id: int
    name: str
    age: int
    email: str
    course: str


class StudentRepository:
    def __init__(self):
        self.index = 0
        self.students = []


class StudentService:
    student_repository = StudentRepository()

    def create_student(self, details):
        details["id"] = self.index
        StudentService.student_repository.students.append(details)
        self.index += 1

    def get_all_students(self):

        return self.students

    def get_student_by_id(self, id):
        for stu in self.students:
            if stu["id"] == id:
                return stu
        return {}

    def update_student(self, student):
        for idx, stu in enumerate(self.students):
            if stu["id"] == student["id"]:
                self.students[idx] = student

    def delete_student(self, id):
        for idx, stu in enumerate(self.students):
            if stu["id"] == id:
                del self.students[idx]
                print("Student deleted successfully.")

    def sort_students(self, bycondition):
        return sorted(self.students, key=lambda item: item[bycondition])


print(
    """
1. Add Student
2. Show All Students
3. Search Student By ID

4. Update Student

5. Delete Student
6. Sort students by age
7. Exit
"""
)
student = Student()
while True:
    x = int(input("Enter Options:"))

    if x == 1:
        name = input("Enter name:")
        age = int(input("Enter age:"))
        email = input("Enter email: ")
        course = input("Enter course: ")

        student.create_student(
            {"name": name, "age": age, "email": email, "course": course}
        )

    elif x == 2:
        students = student.get_all_students()
        for stu in students:
            print(
                f"""
                ID: {stu["id"]}
                Name: {stu["name"]}
                Age: {stu["age"]}
                Email: {stu["email"]}
                Course: {stu["course"]}
                ------------------------
                """
            )

    elif x == 3:
        id = int(input("Enter Student ID"))
        stu = student.get_student_by_id(id)
        print(
            f"""
            ID: {stu["id"]}
            Name: {stu["name"]}
            Age: {stu["age"]}
            Email: {stu["email"]}
            Course: {stu["course"]}
            ------------------------
            """
        )

    elif x == 4:
        id = int(input("Enter Student ID:"))
        name = input("New name:")
        age = int(input("New age:"))
        email = input("New email:")
        course = input("New course:")

        student.update_student(
            {"id": id, "name": name, "age": age, "email": email, "course": course}
        )

    elif x == 5:
        id = int(input("Enter students ID:"))
        student.delete_student(id)

    elif x == 6:
        student.sort_students("age")

    elif x == 7:
        print("Exited")
        break

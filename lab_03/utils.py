import csv
from student import Student
from studentlist import StudentList

class Utils:
    def load_data(self, filename):
        student_list = StudentList()
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        name=row["name"],
                        phone=row["phone"],
                        email=row["email"],
                        group=row["group"]
                    )
                    student_list.add_student(student)
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено. Створено порожній довідник.")
        return student_list

    def save_data(self, filename, student_list):
        with open(filename, mode="w", encoding="utf-8", newline="") as file:
            fieldnames = ["name", "phone", "email", "group"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in student_list.students:
                writer.writerow({
                    "name": student.name,
                    "phone": student.phone,
                    "email": student.email,
                    "group": student.group
                })
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Студент: {self.name}, Вік: {self.age}"



def main():
    students = [
        Student("Zach King", 20),
        Student("Bob Sponge", 18),
        Student("Emma Stone", 21),
        Student("Jon Smith", 19),
        Student("Alice Cooper", 18)
    ]

    print("Відсортовано за ім'ям (A -> Z):")
    for student in sorted(students, key=lambda s: s.name):
        print(f"  {student}")

    print("\nВідсортовано за віком (від молодшого до старшого):")
    for student in sorted(students, key=lambda s: s.age):
        print(f"  {student}")


if __name__ == "__main__":
    main()
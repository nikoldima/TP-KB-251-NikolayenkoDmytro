def main():
    students = [
        {"name": "Zach King", "grade": 78},
        {"name": "Bob Sponge", "grade": 95},
        {"name": "Emma Stone", "grade": 88},
        {"name": "Jon Smith", "grade": 64},
        {"name": "Alice Cooper", "grade": 91}
    ]

    print("Початковий (невідсортований) список:")
    for student in students:
        print(f"  {student['name']}: {student['grade']}")

    sorted_by_name = sorted(students, key=lambda item: item["name"])
    print("\nВідсортовано за ім'ям (A -> Z):")
    for student in sorted_by_name:
        print(f"  {student['name']}: {student['grade']}")

    sorted_by_grade_asc = sorted(students, key=lambda item: item["grade"])
    print("\nВідсортовано за оцінкою (від найменшої до найбільшої):")
    for student in sorted_by_grade_asc:
        print(f"  {student['name']}: {student['grade']}")

    sorted_by_grade_desc = sorted(students, key=lambda item: item["grade"], reverse=True)
    print("\nВідсортовано за оцінкою (від найбільшої до найменшої):")
    for student in sorted_by_grade_desc:
        print(f"  {student['name']}: {student['grade']}")

if __name__ == "__main__":
    main()
import csv
import sys

def add_student(students_list, new_student):
    insert_position = 0
    for item in students_list:
        if new_student["name"] > item["name"]:
            insert_position += 1
        else:
            break
    students_list.insert(insert_position, new_student)
    return students_list
def delete_student(students_list, name):
    for item in students_list:
        if item["name"] == name:
            students_list.remove(item)
            return True  # Успешно удалено
    return False  # Не найдено
def update_student(students_list, old_name, updated_student):
    if delete_student(students_list, old_name):
        add_student(students_list, updated_student)
        return True
    return False



def load_data(filename):
    students = []
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено. Створено порожній довідник.")
    return students


def save_data(filename, students):
    with open(filename, mode="w", encoding="utf-8", newline="") as file:
        fieldnames = ["name", "phone", "email", "group"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)
def print_all(students):
    for elem in students:
        print(
            f"Student name is {elem['name']}, Phone is {elem['phone']}, Email is {elem['email']}, Group is {elem['group']}")
def main():
    if len(sys.argv) < 2:
        print("Помилка: вкажіть ім'я CSV файлу як аргумент командного рядка (наприклад: python lab2.py lab2.csv)")
        sys.exit(1)

    filename = sys.argv[1]
    students = load_data(filename)

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, X exit ] ").strip().upper()

        match choice:
            case "C":
                print("New element will be created:")
                name = input("Please enter student name: ")
                phone = input("Please enter student phone: ")
                email = input("Please enter student email: ")
                group = input("Please enter student group: ")

                new_student = {"name": name, "phone": phone, "email": email, "group": group}
                add_student(students, new_student)
                print("New element has been added")
                print_all(students)

            case "U":
                print("Existing element will be updated")
                old_name = input("Please enter name to be updated: ")

                found = next((item for item in students if item["name"] == old_name), None)

                if found:
                    print("Element found. Enter new data (press Enter to keep old value):")
                    new_name = input(f"New name [{found['name']}]: ") or found['name']
                    new_phone = input(f"New phone [{found['phone']}]: ") or found['phone']
                    new_email = input(f"New email [{found['email']}]: ") or found['email']
                    new_group = input(f"New group [{found['group']}]: ") or found['group']

                    updated_student = {"name": new_name, "phone": new_phone, "email": new_email, "group": new_group}
                    update_student(students, old_name, updated_student)
                    print("Element has been updated")
                else:
                    print("Element was not found")
                print_all(students)

            case "D":
                print("Element will be deleted")
                name = input("Please enter name to be deleted: ")
                if delete_student(students, name):
                    print("Element deleted successfully.")
                else:
                    print("Element was not found.")
                print_all(students)

            case "P":
                print("List will be printed")
                print_all(students)

            case "X":
                print("Saving data to file and Exit()")
                save_data(filename, students)
                break

            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()
import sys
from student import Student
from utils import Utils



def main():
    if len(sys.argv) < 2:
        print("Помилка: вкажіть ім'я CSV файлу як аргумент командного рядка")
        sys.exit(1)

    filename = sys.argv[1]
    utils = Utils()
    student_list = utils.load_data(filename)



    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, X exit ] ").strip().upper()
        match choice:
            case "C":
                print("New element will be created:")
                name = input("Please enter student name: ")
                phone = input("Please enter student phone: ")
                email = input("Please enter student email: ")
                group = input("Please enter student group: ")
                new_student = Student(name, phone, email, group)
                student_list.add_student(new_student)
                print("New element has been added")
                student_list.print_all()
            case "U":
                print("Existing element will be updated")
                old_name = input("Please enter name to be updated: ")
                found = student_list.find_student(old_name)
                if found:
                    print("Element found. Enter new data (press Enter to keep old value):")
                    new_name = input(f"New name [{found.name}]: ") or found.name
                    new_phone = input(f"New phone [{found.phone}]: ") or found.phone
                    new_email = input(f"New email [{found.email}]: ") or found.email
                    new_group = input(f"New group [{found.group}]: ") or found.group
                    updated_student = Student(new_name, new_phone, new_email, new_group)
                    student_list.update_student(old_name, updated_student)
                    print("Element has been updated")
                else:
                    print("Element was not found")
                student_list.print_all()
            case "D":
                print("Element will be deleted")
                name = input("Please enter name to be deleted: ")
                if student_list.delete_student(name):
                    print("Element deleted successfully.")
                else:
                    print("Element was not found.")
                student_list.print_all()
            case "P":
                print("List will be printed")
                student_list.print_all()
            case "X":
                print("Saving data to file and Exit()")
                utils.save_data(filename, student_list)
                break
            case _:
                print("Wrong choice")



if __name__ == "__main__":
    main()
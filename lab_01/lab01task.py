list = [
    {"name": "Bob Sponge", "phone": "0631234567", "email": "bobsponge@gmail.com", "group": "KB-251"},
    {"name": "Emma Stone", "phone": "0631234567", "email": "emmastone@gmail.com", "group": "KB-251"},
    {"name": "Jon Smith", "phone": "0631234567", "email": "jonsmith@gmail.com", "group": "KB-251"},
    {"name": "Zach King", "phone": "0631234567", "email": "zachking@gmail.com", "group": "KB-251"}
]

def printAllList():
    for elem in list:
        strForPrint = f"Student name is {elem['name']}, Phone is {elem['phone']}, Email is {elem['email']}, Group is {elem['group']}"
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")

    newItem = {"name": name, "phone": phone, "email": email, "group": group}

    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(deletePosition))
        del list[deletePosition]
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    updatePosition = -1

    for item in list:
        if name == item["name"]:
            updatePosition = list.index(item)
            break

    if updatePosition == -1:
        print("Element was not found")
    else:
        print("Element found. Enter new data (press Enter to keep old value):")
        current = list[updatePosition]

        new_name = input(f"New name [{current['name']}]: ")
        if new_name == "": new_name = current['name']

        new_phone = input(f"New phone [{current['phone']}]: ")
        if new_phone == "": new_phone = current['phone']

        new_email = input(f"New email [{current['email']}]: ")
        if new_email == "": new_email = current['email']

        new_group = input(f"New group [{current['group']}]: ")
        if new_group == "": new_group = current['group']

        del list[updatePosition]
        newItem = {"name": new_name, "phone": new_phone, "email": new_email, "group": new_group}

        insertPosition = 0
        for item in list:
            if new_name > item["name"]:
                insertPosition += 1
            else:
                break
        list.insert(insertPosition, newItem)
        print("Element has been updated")
    return

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated:")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong choose")
main()
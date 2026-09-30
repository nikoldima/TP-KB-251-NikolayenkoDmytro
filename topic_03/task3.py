student = {"name": "Dmytro", "age": 18, "course": 2}
print(f"Початковий словник: {student}")

student.update({"group": "TP-KB-251", "age": 19})
print(f"Після update(): {student}")

del student["course"]
print(f"Після del student['course']: {student}")

print(f"Ключі (keys): {list(student.keys())}")

print(f"Значення (values): {list(student.values())}")

print(f"Пари (items): {list(student.items())}")

student.clear()
print(f"Після clear(): {student}")
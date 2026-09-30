def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    if b == 0:
        return "Помилка! Ділення на нуль."
    return a / b

print("=== Безкінечний калькулятор ===")
print("Для виходу введіть 'q' або 'exit' замість операції.\n")

while True:
    op = input("Введіть операцію (+, -, *, /): ")

    if op == 'q' or op == 'exit':
        print("Програма завершена. До побачення!")
        break

    if op not in ['+', '-', '*', '/']:
        print("Невідома операція, спробуйте ще раз.\n")
        continue

    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))

    match op:
        case '+':
            res = add(a, b)
        case '-':
            res = sub(a, b)
        case '*':
            res = mult(a, b)
        case '/':
            res = div(a, b)

    print(f"Результат: {res}\n")
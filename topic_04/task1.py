def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b



def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Помилка! Ділення на нуль (перехоплено ZeroDivisionError)."


def get_number(prompt_text):
    while True:
        try:
            user_input = input(prompt_text)
            return float(user_input)
        except ValueError:
            print("Помилка! Ви ввели текст замість числа. Спробуйте ще раз.")

print("=== Безкінечний калькулятор (Topic 04) ===")
print("Для виходу введіть 'q' або 'exit'.\n")

while True:
    op = input("Введіть операцію (+, -, *, /): ")

    if op == 'q' or op == 'exit':
        print("Програма завершена. До побачення!")
        break
    if op not in ['+', '-', '*', '/']:
        print("Невідома операція, спробуйте ще раз.\n")
        continue

    a = get_number("Введіть перше число: ")
    b = get_number("Введіть друге число: ")


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
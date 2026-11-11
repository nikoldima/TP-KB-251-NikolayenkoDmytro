from functions import add, sub, mult, div
from operations import get_number, get_operation


def main():
    print("=== Модульний калькулятор ===")

    while True:
        op = get_operation()

        if op == 'q' or op == 'exit':
            print("Програма завершена. До побачення!")
            break

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


if __name__ == "__main__":
    main()
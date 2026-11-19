import logging
from functions import add, sub, mult, div
from operations import get_number, get_operation


logging.basicConfig(
    filename="calc.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)



def main():
    logging.info("=== Запуск програми калькулятор ===")
    print("=== Модульний калькулятор з логуванням ===")

    while True:
        op = get_operation()

        if op == 'q' or op == 'exit':
            logging.info("=== Завершення роботи програми ===")
            print("Програма завершена. До побачення")
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

        logging.info(f"Виконано операцію: {a} {op} {b} | Результат: {res}")
        print(f"Результат: {res}\n")

if __name__ == "__main__":
    main()
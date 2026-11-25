from rpn import calculate

def main():
    print("=== Калькулятор математичних виразів (ЗПЗ) ===")
    print("Підтримувані операції: +, -, *, /, ^ та дужки ( )")
    print("Для виходу введіть 'q' або 'exit'\n")

    while True:
        expr = input("Введіть математичний вираз: ").strip()
        if expr.lower() in ("q", "exit"):
            print("Роботу програми завершено")
            break

        try:
            rpn_str, result = calculate(expr)
            print(f"1. Зворотний польський запис (ЗПЗ): {rpn_str}")
            print(f"2. Результат обчислення: {result}\n")
        except (ValueError, ZeroDivisionError) as err:
            print(f"Помилка: {err}\n")

if __name__ == "__main__":
    main()
import logging

def get_number(prompt_text):
    while True:
        user_input = input(prompt_text)
        try:
            value = float(user_input)
            logging.info(f"Користувач ввів число: {value}")
            return value
        except ValueError:
            logging.warning(f"Некоректне введення числа: '{user_input}'")
            print("Помилка! Ви ввели текст замість числа. Спробуйте ще раз")

def get_operation():
    while True:
        op = input("Введіть операцію (+, -, *, /) або 'q' для виходу: ").strip().lower()
        if op in ['+', '-', '*', '/', 'q', 'exit']:
            logging.info(f"Користувач обрав дію: '{op}'")
            return op
        logging.warning(f"Невідома операція: '{op}'")
        print("Невідома операція, спробуйте ще раз")
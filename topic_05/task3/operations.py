def get_number(prompt_text):
    while True:
        try:
            user_input = input(prompt_text)
            return float(user_input)
        except ValueError:
            print("Помилка! Ви ввели текст замість числа. Спробуйте ще раз.")

def get_operation():
    while True:
        op = input("Введіть операцію (+, -, *, /) або 'q' для виходу: ").strip().lower()
        if op in ['+', '-', '*', '/', 'q', 'exit']:
            return op
        print("Невідома операція, спробуйте ще раз.")
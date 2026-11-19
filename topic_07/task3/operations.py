class UserInterface:
    def get_number(self, prompt_text):
        while True:
            try:
                return float(input(prompt_text))
            except ValueError:
                print("Помилка! Ви ввели текст замість числа. Спробуйте ще раз")

    def get_operation(self):
        while True:
            op = input("Введіть операцію (+, -, *, /) або 'q' для виходу: ").strip().lower()
            if op in ['+', '-', '*', '/', 'q', 'exit']:
                return op
            print("Невідома операція, спробуйте ще раз")
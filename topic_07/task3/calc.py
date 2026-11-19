from functions import MathOperations
from operations import UserInterface



class Calculator:
    def __init__(self):
        self.math = MathOperations()
        self.ui = UserInterface()

    def run(self):
        print("=== ООП Калькулятор ===")
        while True:
            op = self.ui.get_operation()

            if op in ['q', 'exit']:
                print("Програма завершена. До побачення!")
                break

            a = self.ui.get_number("Введіть перше число: ")
            b = self.ui.get_number("Введіть друге число: ")

            match op:
                case '+':
                    res = self.math.add(a, b)
                case '-':
                    res = self.math.sub(a, b)
                case '*':
                    res = self.math.mult(a, b)
                case '/':
                    res = self.math.div(a, b)
            print(f"Результат: {res}\n")



if __name__ == "__main__":
    app = Calculator()
    app.run()
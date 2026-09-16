def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    if b == 0:
        return "Ділити на нуль не можна."
    else:
        return a / b

def calculator_match(a, b, op):
    match op:
        case '+':
            res = add(a, b)
        case '-':
            res = sub(a, b)
        case '*':
            res = mult(a, b)
        case '/':
            res = div(a, b)
        case _:
            res = "Невідома операція"
    return res

print("Калькулятор через match:")
print(calculator_match(10, 5, '*'))
print(calculator_match(10, 0, '/'))
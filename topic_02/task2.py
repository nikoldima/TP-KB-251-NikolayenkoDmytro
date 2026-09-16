def do_plus(a, b):
    return a + b
def do_minus(a, b):
    return a - b
def do_mult(a, b):
    return a * b
def do_div(a, b):
    if b == 0:
        return "Ділити на нуль не можна."
    else:
        return a / b

def calculator_if(a, b, op):
    if op == '+':
        res = do_plus(a, b)
    elif op == '-':
        res = do_minus(a, b)
    elif op == '*':
        res = do_mult(a, b)
    elif op == '/':
        res = do_div(a, b)
    else:
        res = "Невідома операція"
    return res

x = 14
y = 88
operation = '+'

результат = calculator_if(x, y, operation)
print(f"Результат {x} {operation} {y} = {результат}")
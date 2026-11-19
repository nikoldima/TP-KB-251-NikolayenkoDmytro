import logging

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
        logging.error(f"Спроба ділення на нуль: {a} / {b}")
        return "Помилка! Ділення на нуль"
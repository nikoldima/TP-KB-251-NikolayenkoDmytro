OPERATORS = {
    "+": (1, "L"),
    "-": (1, "L"),
    "*": (2, "L"),
    "/": (2, "L"),
    "^": (3, "R"),
}



def tokenize(expression: str) -> list[str]:

    tokens = []
    i = 0
    n = len(expression)

    while i < n:
        ch = expression[i]

        if ch.isspace():
            i += 1
            continue



        is_unary_minus = (
            ch == "-"
            and (not tokens or tokens[-1] in OPERATORS or tokens[-1] == "(")
        )

        if ch.isdigit() or ch == "." or (is_unary_minus and i + 1 < n and (expression[i + 1].isdigit() or expression[i + 1] == ".")):
            num_chars = [ch]
            i += 1
            dot_count = 1 if ch == "." else 0
            while i < n and (expression[i].isdigit() or expression[i] == "."):
                if expression[i] == ".":
                    dot_count += 1
                    if dot_count > 1:
                        raise ValueError(f"Некоректний формат числа у виразі: '{''.join(num_chars)}'")
                num_chars.append(expression[i])
                i += 1
            tokens.append("".join(num_chars))
            continue

        if is_unary_minus and i + 1 < n and expression[i + 1] == "(":
            tokens.extend(["0", "-"])
            i += 1
            continue

        if ch in OPERATORS or ch in ("(", ")"):
            tokens.append(ch)
            i += 1
            continue

        raise ValueError(f"Невідомий символ у виразі: '{ch}'")

    return tokens





def is_number(token: str) -> bool:
    try:
        float(token)
        return True
    except ValueError:
        return False


def to_rpn(expression: str) -> list[str]:

    tokens = tokenize(expression)
    if not tokens:
        raise ValueError("Порожній математичний вираз")

    output = []
    stack = []

    for token in tokens:
        if is_number(token):
            output.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if not stack:
                raise ValueError("Неузгоджені дужки: зайва закриваюча дужка ')'")
            stack.pop()
        elif token in OPERATORS:
            prec1, assoc1 = OPERATORS[token]
            while stack and stack[-1] in OPERATORS:
                prec2, _ = OPERATORS[stack[-1]]
                if (assoc1 == "L" and prec1 <= prec2) or (assoc1 == "R" and prec1 < prec2):
                    output.append(stack.pop())
                else:
                    break
            stack.append(token)



    while stack:
        top = stack.pop()
        if top in ("(", ")"):
            raise ValueError("Неузгоджені дужки: не закрита дужка '('")
        output.append(top)

    return output


def evaluate_rpn(rpn_tokens: list[str]) -> float:

    stack = []

    for token in rpn_tokens:
        if is_number(token):
            stack.append(float(token))
        elif token in OPERATORS:
            if len(stack) < 2:
                raise ValueError("Некоректний вираз: недостатньо операндів для операції")
            b = stack.pop()
            a = stack.pop()

            match token:
                case "+":
                    stack.append(a + b)
                case "-":
                    stack.append(a - b)
                case "*":
                    stack.append(a * b)
                case "/":
                    if b == 0:
                        raise ZeroDivisionError("Помилка: ділення на нуль")
                    stack.append(a / b)
                case "^":
                    stack.append(a ** b)

    if len(stack) != 1:
        raise ValueError("Некоректний математичний вираз")


    return stack[0]


def calculate(expression: str) -> tuple[str, float]:
    rpn_tokens = to_rpn(expression)
    result = evaluate_rpn(rpn_tokens)
    return " ".join(rpn_tokens), result
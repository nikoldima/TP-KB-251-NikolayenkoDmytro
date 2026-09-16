import math

def find_discriminant(a, b, c):
    d = (b ** 2) - (4 * a * c)
    return d
def find_roots(a, b, c):
    d = find_discriminant(a, b, c)

    print(f"Шукаємо корені для рівняння з a={a}, b={b}, c={c}")
    print(f"Дискримінант дорівнює: {d}")

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"Два корені: x1 = {x1}, x2 = {x2}")
    elif d == 0:
        x = -b / (2 * a)
        print(f"Один корінь: x = {x}")
    else:
        print("Дискримінант менше нуля. Коренів немає.")

find_roots(1, -5, 6)
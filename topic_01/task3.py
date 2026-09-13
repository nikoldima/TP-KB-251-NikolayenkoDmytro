def find_discriminant(a, b, c):
    return b**2 - 4*a*c

a, b, c = 1, -5, 6
d = find_discriminant(a, b, c)
print(f"Дискримінант для рівняння {a}x^2 + {b}x + {c} = 0 дорівнює: {d}")
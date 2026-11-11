import random



def main():
    choices = ["stone", "scissor", "paper"]

    print("=== Гра: Камінь, ножиці, папір ===")
    user_choice = input('Введіть ваш вибір ("stone", "scissor" або "paper"): ').strip().lower()

    if user_choice not in choices:
        print("Помилка: Неправильний ввід.")
        return

    comp_choice = random.choice(choices)
    print(f"Комп'ютер вибрав: {comp_choice}")

    if user_choice == comp_choice:
        print("Результат: Нічия!")
    elif (user_choice == "stone" and comp_choice == "scissor") or \
            (user_choice == "scissor" and comp_choice == "paper") or \
            (user_choice == "paper" and comp_choice == "stone"):
        print("Результат: Ви перемогли!")
    else:
        print("Результат: Комп'ютер переміг!")



if __name__ == "__main__":
    main()
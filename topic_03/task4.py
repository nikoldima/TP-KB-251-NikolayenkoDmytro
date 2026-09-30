def find_insert_position(sorted_list, new_element):

    for i in range(len(sorted_list)):
        if sorted_list[i] >= new_element:
            return i
    return len(sorted_list)



numbers = [10, 20, 30, 40, 50]
value_to_insert = 35

print(f"Відсортований список: {numbers}")
print(f"Нове число: {value_to_insert}")

pos = find_insert_position(numbers, value_to_insert)
print(f"Позиція для вставки: індекс {pos}")

numbers.insert(pos, value_to_insert)
print(f"Список після вставки: {numbers}")
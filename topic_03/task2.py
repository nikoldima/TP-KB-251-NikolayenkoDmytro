my_list = [10, 20, 30]
print(f"Початковий список: {my_list}")

my_list.append(40)
print(f"Після append(40): {my_list}")

my_list.extend([50, 60])
print(f"Після extend([50, 60]): {my_list}")

my_list.insert(2, 99)
print(f"Після insert(2, 99): {my_list}")

my_list.remove(99)
print(f"Після remove(99): {my_list}")

my_list.sort()
print(f"Після sort(): {my_list}")

my_list.reverse()
print(f"Після reverse(): {my_list}")

list_copy = my_list.copy()
print(f"Після copy(), ось наша копія: {list_copy}")

my_list.clear()
print(f"Після clear(): {my_list}")
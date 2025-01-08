
# Задание task_02_30.
#
# Выполнил: Фамилия И.О.
# Группа: !!!



# Все разделенные пробелом элементы будут преобразованы в список целых чисел
nums = [int(item) for item in input().split()]

# 1. Все положительные
for item in nums:
    if item <= 0:
        all_pos_1 = False
        break
else:
    all_pos_1 = True

all_pos_2 = all([item > 0 for item in nums])

# 2. Хотя бы 1 нулевой элемент
for item in nums:
    if item == 0:
        any_zero_1 = True
        break
else:
    any_zero_1 = False

any_zero_2 = any([item == 0 for item in nums])

# 3. Все четные
# Удалите комментарий и допишите код (определите переменные all_even_1, all_even_2)

# 4. Хотя бы 1 нечетный элемент
# Удалите комментарий и допишите код (any_odd_1, any_odd_2)

print("Все положительные:", all_pos_1, all_pos_2)
print("Хотя бы 1 нулевой элемент:", any_zero_1, any_zero_2)
print("Все четные:", all_even_1, all_even_2)
print("Хотя бы 1 нечетный элемент:", any_odd_1, any_odd_2)

# --------------
# Пример вывода:
#
# -1 1 100 0
# Все положительные: False False
# Хотя бы 1 нулевой элемент: True True
# Все четные: False False
# Хотя бы 1 нечетный элемент: True True

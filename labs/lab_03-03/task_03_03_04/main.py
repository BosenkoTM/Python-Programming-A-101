
# Задание task_03_03_04.
#
# Выполнил: Фамилия И.О.
# Группа: !!!



"""
Ошибки (номера строк через пробел, данная строка - №2): !!!
"""


def min_pair(nums):
    """Вернуть минимальную сумму соседних 2-х чисел в списке 'nums'."""
    min = nums[0] * nums[1]
    for i in range(2, len(nums)):
        min = min(nums[i] + nums[i + 1], min)

    return min

# import random
#
# random.seed(50)
#
# N_MAX = 10
# RANGE_MIN = 1
# RANGE_MAX = 100
# nums = random.sample(range(RANGE_MIN, RANGE_MAX), N_MAX)
#
# print(nums)
#
# print(min_pair(nums))

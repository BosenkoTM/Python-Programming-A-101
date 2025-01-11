
# Задание task_03_02_04.
#
# Выполнил: Фамилия И.О.
# Группа: !!!



def foo(n):
    """!!!

    Параметры:
        - n (int): число.

    Сложность: !!!.
    """
    res = []
    for i in range(1, n + 1):
        divisors = 0
        j = 2
        while j < i and divisors == 0:
            if i % j == 0:
                divisors += 1
            j += 1

        if divisors == 0:
            res.append(i)

    return res

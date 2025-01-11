
# Задание task_03_02_03.
#
# Выполнил: Фамилия И.О.
# Группа: !!!



def foo(s):
    """!!!

    Параметры:
        - s (str): строка.

    Сложность: !!!.
    """
    val = 0
    for c in s:
        if c.isdigit():
            val += int(c)
    return val

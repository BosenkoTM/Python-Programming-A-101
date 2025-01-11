
# Задание task_03_02_02.
#
# Выполнил: Фамилия И.О.
# Группа: !!!



def foo(i):
    """!!!

    Параметры:
        - i (int): число.

    Сложность: !!!.
    """
    digits = "0123456789"
    if i == 0:
        return "0"
    result = ""
    while i > 0:
        result = digits[i%10] + result
        i = i // 10
    return result

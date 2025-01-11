
# Задание task_03_02_07.
#
# Выполнил: Фамилия И.О.
# Группа: !!!



def foo(low, high):
    """!!!

    Параметры:
        - low (int): нижняя граница;
        - high (int): верхняя граница.

    Сложность: !!!.
    """
    guessing = True
    while guessing:
        guess = (low + high) // 2
        print("Загаданное число {0}?".format(guess))
        pointer = input(
            "Введите '+', если Ваше число меньше.\n"
            "Введите '-' если Ваше число больше.\n"
            "Введите '=', если я угадал.\n").lower()
        if pointer == "+":
            high = guess
        elif pointer == "-":
            low = guess
        elif pointer == "=":
            guessing = False
        else:
            print("Введите '+', '-' или '='.")

    return guess


# ЗАКОММЕНТИРУЙТЕ этот код перед запуском проверки
# low, high = 0, 100
# print("Пожалуйста, загадайте число от {0} до {1}!".format(low, high))
# guess = foo(low, high)
# print("Игра окончена, Вы загадали число: {0}.".format(guess))

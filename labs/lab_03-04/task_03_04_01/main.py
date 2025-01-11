
# Задание task_03_04_01.
#
# Выполнил: Фамилия И.О.
# Группа: !!!



def load_data():
    """Вернуть список вещественных чисел, введенных с клавиатуры.

    Числа вводятся в одной строке."""
    # Удалите комментарий и допишите код


def save_data(values, filename):
    """Записать данные в файл.

    Параметры:
        - values (list of float): список вещественных чисел;
        - filename (str): имя файла.

    Функция не обрабатывает исключения.
    """
    # Удалите комментарий и допишите код


try:
    filename = # Удалите комментарий и допишите код (ввести имя с клавиатуры)
    values = load_data()
    save_data(values, filename)

except ValueError as err:
    print("Числа были введены с ошибкой.")

except (OSError, IOError) as err:
    print("Ошибка при сохранении файла с данными:", err)

except Exception as err:
    print("Произошла ошибка!")
    print("Тип:", type(err))
    print("Описание:", err)

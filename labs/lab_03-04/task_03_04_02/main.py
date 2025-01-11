
# Задание task_03_04_02.
#
# Выполнил: Фамилия И.О.
# Группа: !!!



def load_data(filename):
    """Загрузить список вещественных чисел из файла 'filename'.

    Функция не обрабатывает исключения."""
    # Удалите комментарий и допишите код


def append_to_file(values, filename):
    """Дописать данные в файл.

    Параметры:
        - values (list of float): список вещественных чисел;
        - filename (str): имя файла.
    """
    # Удалите комментарий и допишите код


try:
    filename = # Удалите комментарий и допишите код (ввести имя с клавиатуры)
    values = load_data(filename)

    # Удалите комментарий и допишите код
    append_to_file(# Удалите комментарий и допишите код, filename)

except FileNotFoundError as err:
    print("Указанный файл не существует.")

except (IOError, ValueError) as err:
    print("Ошибка при чтении/сохранении файла с данными:", err)

except Exception as err:
    print("Произошла ошибка!")
    print("Тип:", type(err))
    print("Описание:", err)

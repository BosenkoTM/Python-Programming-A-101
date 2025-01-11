
# Задание task_03_04_08.
#
# Выполнил: Фамилия И.О.
# Группа: !!!



import csv
import json


class NoSuchYearError(Exception):
    def __init__(self, message):
        super().__init__(message)


def load_data(filename):
    """Загрузить данные по болезням из csv-файла 'filename'.

    Параметры:
        - filename (str): имя файла.

    Результат:
        - list of list, где первый элемент - список заголовков.

    Числовые значения должны быть преобразованы из строк в числа.

    Функция не обрабатывает исключения."""
    data = []
    # Загрузка файла
    # Удалите комментарий и допишите код

    # Преобразование строк в числа
    # Удалите комментарий и допишите код

    return data


def export(filename, data, year_1, year_2):
    """Сохранить данные 'data' в json-файл 'filename' выполнив группировку
    по возрасту и сравнив годы 'year_1' и 'year_2'.

    Параметры:
        - filename (str): имя файла;
        - data (list of list): структура данных формата 'load_data()';
        - year_1 (int): первый год для анализа;
        - year_2 (int): второй год для анализа.

    Исключения:
        - NoSuchYearError: 'year_1' или 'year_2' не существует.

    Необходимо сформировать и записать в файл 'filename' словарь вида:

    {
     "Второй год": {

        "Взрослые": [
           {
             класс болезни: значение
           },
           ...
        ],

        "Дети": [
           {
             класс болезни: значение
           },
           ...
        ]
     },

     "Изменения": {

        "Взрослые": [
           {
             класс болезни: значение в %
           },
           ...
        ],

        "Дети": [
           {
             класс болезни: значение в %
           },
           ...
        ]
      }
    }

    ...

    где группа "Второй год" содержит данные по 'year_2', а "Изменения" -
    процентное изменение 'year_1' -> 'year_2'.

    Все значения приводятся в порядке убывания с округлением процентов
    до 2-х знаков после запятой.

    """
    # Проверка параметров 'year_1' и 'year_2'
    # Удалите комментарий и допишите код

    # Формирование списков
    # data_year_2_sorted_adult
    # data_year_2_sorted_children
    # data_changes_sorted_adult
    # data_changes_sorted_children
    # Удалите комментарий и допишите код

    res = {
        "Второй год": {
            "Взрослые": data_year_2_sorted_adult,
            "Дети": data_year_2_sorted_children
        },

        "Изменения": {
            "Взрослые": data_changes_sorted_adult,
            "Дети": data_changes_sorted_children
        }
    }

    # Сохранение в файл
    # Удалите комментарий и допишите код


# Добавьте в код обработку исключений

# filename = input("Введите имя файла: ")
filename = "medical_stats.csv"

# export_filename = input("Введите имя файла: ")
export_filename = "output.json"

data = load_data(filename)
# print(data)

print("Доступные годы для анализа:", data[0][1:-1])
# year_1, year_2 = [int(x) for x in
#                   input("Введите два года через пробел: ")).split()]
year_1, year_2 = 2014, 2015

export(export_filename, data, year_1, year_2)


# Задание task_03_04_07.
#
# Выполнил: Фамилия И.О.
# Группа: !!!



import csv


class NoSuchCountryError(Exception):
    def __init__(self, message):
        super().__init__(message)


class IllegalArgumentError(ValueError):
    pass


def load_data(filename):
    """Загрузить данные ВВП на душу населения из csv-файла 'filename'.

    Если значения для какого-либо государства не известно, строка должна
    быть пропущена и отсутствовать в результате.

    Параметры:
        - filename (str): имя файла.

    Результат:
        - list of dict: [
            {
              - "name": str: название государства;
              - "gdp": float: ВВП на душу населения.
            }
            ...
          ]

    Функция не обрабатывает исключения."""
    # Удалите комментарий и допишите код


def search(data, criteria):
    """Выполнить поиск государства-значения в 'data' по критерию 'criteria'.

    Параметры:
        - data (list of dict): структура данных формата 'load_data()';
        - criteria (string): критерий поиска; допустимые значения:
            - "-max-": государство с максимальным ВВП на душу населения;
            - "-min-": государство с мнимальным ВВП на душу населения;
            - "Russian Federation": название государства.

    Результат:
        - dict: [
            {
              - "name": str: название государства;
              - "gdp": float: ВВП на душу населения.
            }
        или
        - NoSuchCountryError: если такой страны нет.
    """
    # Определение операции
    if criteria == "-max-":
    # Удалите комментарий и допишите код

        raise NoSuchCountryError(
            "Значение параметра 'criteria' может быть "
            "одним из:\n"
            '- "-max-": государство с максимальным ВВП на душу населения;\n'
            '- "-min-": государство с мнимальным ВВП на душу населения;\n'
            '- "Russian Federation": название государства.')


def save_data(filename, data, criteria):
    """Сохранить данные 'data' в csv-файл 'filename' по критерию 'criteria'.

    Параметры:
        - filename (str): имя файла;
        - data (list of dict): структура данных формата 'load_data()';
        - criteria (string): критерий поиска; допустимые значения:
            - "top=X": первые X государств по ВВП на душу населения
                         (целое число > 0, по убыванию значения);
            - "tail=X": последние X государств по ВВП на душу населения
                          (целое число > 0, по возрастанию значения);
            - "greater=X": список государств с ВВП на душу населения, больше
                           чем X (вещ. число, по убыванию значения);
            - "less=X": список государств с ВВП на душу населения, меньше
                          чем X (вещ. число, по возрастанию значения).

    Исключения:
        - IllegalArgumentError: 'criteria' содержит недопустимое значение.
    """
    try:
        method, value = criteria.split("=")
        filtered_data = []

        # Определение операции
        # Удалите комментарий и допишите код

        # Сохранение в файл
        # Удалите комментарий и допишите код

    except Exception as err:
        raise IllegalArgumentError(
            "Значение параметра 'criteria' может быть "
            "одним из:\n"
            '- "top=X": первые X государств по ВВП на душу населения'
            ' (целое число > 0, по убыванию значения);\n'
            '- "tail=X": последние X государств по ВВП на душу населения'
            ' (целое число > 0, по возрастанию значения);\n'
            '- "greater=X": список государств с ВВП на душу населения, больше'
            ' чем X (вещ. число, по убыванию значения);\n'
            '- "less=X": список государств с ВВП на душу населения, меньше'
            ' чем X (вещ. число, по возрастанию значения).')


# Добавьте в код обработку исключений

filename = input("Введите имя файла: ")
# filename = "gdp_per_capita_2016.csv"

save_filename = input("Введите имя файла: ")
# save_filename = "output.csv"

data = load_data(filename)
# print(data)

print(search(data, criteria="-max-"))
print(search(data, criteria="-min-"))
print(search(data, criteria="Russian Federation"))

save_data(save_filename, data, criteria="top=5")
# save_data(save_filename, data, criteria="tail=5")
# save_data(save_filename, data, criteria="greater=5000.50")
# save_data(save_filename, data, criteria="less=5000.50")

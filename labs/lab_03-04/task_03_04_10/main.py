
# Задание task_03_04_10.
#
# Выполнил: Фамилия И.О.
# Группа: !!!
# E-mail: !!!


import json


class IllegalArgumentError(ValueError):
    pass


def load_phonebook(filename):
    """Загрузить данные телефонной книги из json-файла 'filename'.

    Параметры:
        - filename (str): имя файла.

    Результат:
        - list of dict.

    Функция не обрабатывает исключения."""
    # Удалите комментарий и допишите код


def save_phonebook(filename, phonebook):
    """Сохранить телефонную книгу 'phonebook' в json-файл 'filename'.

    Параметры:
        - filename (str): имя файла;
        - phonebook (list of dict): телефонная книга.

    Функция не обрабатывает исключения."""
    # Удалите комментарий и допишите код


def search_by_name(phonebook, name):
    """Вернуть записи в телефонной книге, в имена которых входит 'name'
    (без учета регистра).

    Параметры:
        - phonebook (list of dict): телефонная книга;
        - name (str): имя контакта (не пустое).

    Результат:
        - list of dict.

    Исключения:
        - IllegalArgumentError: нарушение типа или содержимого 'name'.
    """
    # Удалите комментарий и допишите код


def search_by_phone(phonebook, phone_number):
    """Вернуть записи в телефонной книге, телефоны которых содержат
    'phone_number'.

    Параметры:
        - phonebook (list of dict): телефонная книга;
        - phone_number (str): номер телефона (не пустой).

    Результат:
        - list of dict.

    Исключения:
        - IllegalArgumentError: нарушение типа или содержимого 'phone_number'.
    """
    # Удалите комментарий и допишите код


def add_record(phonebook, name, phones):
    """Добавить в телефонную книгу запись с именем 'name' и списком
    телефонов 'phones'.

    Параметры:
        - phonebook (list of dict): телефонная книга;
        - name (str): имя (не пустое);
        - phones (list of dict): список телефонных номеров с описанием вида:
                                    {
                                        "описание": "мобильный",
                                        "номер": "+7111000043"
                                    }
                                 значения не должны быть пустыми.

    Результат:
        - phonebook (list of dict): телефонная книга.

    Исключения:
        - IllegalArgumentError:
          нарушение типа или содержимого 'name' или 'phones'.
    """
    # Удалите комментарий и допишите код


def remove_name(phonebook, name):
    """Удалить из телефонной книги все контакты, содержащие 'name'
    (без учета регистра).

    Параметры:
        - phonebook (list of dict): телефонная книга;
        - name (str): имя (не пустое).

    Исключения:
        - IllegalArgumentError: нарушение типа или содержимого 'name'.
    """
    # Удалите комментарий и допишите код


def remove_phone(phonebook, phone_number):
    """Удалить из телефонной книги все телефоны, содержащие 'phone'.

    Параметры:
        - phonebook (list of dict): телефонная книга;
        - phone_number (str): номер телефона (не пустой).

    Результат:
        - phonebook (list of dict): телефонная книга.

    Исключения:
        - IllegalArgumentError: нарушение типа или содержимого 'phone_number'.
    """
    # Удалите комментарий и допишите код


def pretty_print(data):
    print(json.dumps(data, ensure_ascii=False, indent=2))


# Операции ниже выполняют тестирование реализованных функций
# Закомментируйте/раскомментируйте необходимые операции

filename = "phonebook.json"

phonebook = load_phonebook(filename)
# pretty_print(phonebook)

# Поиск
search_res = search_by_name(phonebook, "ВА")
# pretty_print(search_res)
assert len(search_res) == 3

search_res = search_by_phone(phonebook, "9")
# pretty_print(search_res)
assert len(search_res) == 2

# Добавление
assert len(search_by_name(phonebook, "Павлова Алиса")) == 0
phonebook = add_record(phonebook, "Павлова Алиса", [
    {
        "описание": "мобильный",
        "номер": "+7111000033"
    }
])
assert len(search_by_name(phonebook, "Павлова Алиса")) == 1

phonebook = add_record(phonebook, "Семенов Семен", [
    {
        "описание": "мобильный",
        "номер": "+7111000043"
    },
    {
        "описание": "мобильный 2",
        "номер": "+7222000333"
    }
])
assert len(search_by_name(phonebook, "Семенов Семен")) == 1

# Удаление
phonebook = remove_phone(phonebook, "33")
assert len(search_by_phone(phonebook, "7111000033")) == 0
assert len(search_by_phone(phonebook, "7222000333")) == 0

phonebook = remove_name(phonebook, "Семенов Семен")
assert len(search_by_name(phonebook, "Семен")) == 0

# pretty_print(phonebook)

# save_phonebook(filename, phonebook)

print("Основные операции работают успешно.")

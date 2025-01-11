
# Задание task_03_03_06.
#
# Выполнил: Фамилия И.О.
# Группа: !!!



"""
Ошибки (номера строк через пробел, данная строка - №2): !!!
"""


def unemployment_rate(unemployed, employed):
    """Вернуть уровень безработицы (УБ) в долях 1.

       Расчет по формуле: УБ = Безработные / (Занятые + Безработные).
    """
    return unemployed / (unemployed + employed)


unemployed = int(input("Введите кол-во безработных (чел.): "))
employed = int(input("Введите кол-во занятых (чел.): "))
rate = unemployment_rate(unemployed, employed)
print("Уровень безработицы = {:.1%}".format(rate))

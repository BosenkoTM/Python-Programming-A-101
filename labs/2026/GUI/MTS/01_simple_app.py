import sys
# Импортируем базовые классы для работы с интерфейсом
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize

# Тема. Создание первого окна, жизненный цикл приложения и обработка нажатий (Signals & Slots).
# Цель. Понять роль QApplication, QMainWindow , познакомиться с циклом обработки событий (Event Loop)  и связать событие клика с функцией.

# Создаем главный класс нашего окна, наследуясь от QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 1. Установка заголовка окна
        self.setWindowTitle("Мое первое GUI-приложение")

        # 2. Создание виджета кнопки
        self.button = QPushButton("Нажми меня!")

        # Делаем кнопку переключаемой (хранит состояние Нажата/Отжата)
        self.button.setCheckable(True)

        # 3. Связываем сигналы кнопки со слотами (нашими функциями)
        # Сигнал clicked отправляет значение True/False, если кнопка checkable
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.clicked.connect(self.the_button_was_toggled)

        # Устанавливаем кнопку как центральный виджет окна
        self.setCentralWidget(self.button)

        # 4. Управляем размерами окна (ширина, высота)
        self.setFixedSize(QSize(400, 300))  # Фиксирует размер окна, запрещая растягивание

    # Слот 1. Вызывается при нажатии
    def the_button_was_clicked(self):
        print("Клик зафиксирован в консоли!")

    # Слот 2. Получает состояние кнопки (нажата/отжата)
    def the_button_was_toggled(self, checked):
        print("Текущее состояние кнопки (Checked):", checked)


# Точка входа в программу
if __name__ == "__main__":
    # QApplication управляет ресурсами и циклом событий. Передаем аргументы запуска sys.argv
    app = QApplication(sys.argv)

    # Создаем экземпляр нашего окна
    window = MainWindow()

    # Окна скрыты по умолчанию, их нужно явно отобразить
    window.show()

    # Запускаем цикл обработки событий. Программа будет работать, пока мы не закроем окно.
    sys.exit(app.exec())

# Практическое задание:
#    Измените код так, чтобы при первом нажатии текст на кнопке менялся на «Кнопка нажата!», а сама кнопка становилась неактивной (используйте self.button.setEnabled(False)).
#    Измените фиксированный размер окна на динамический с установкой минимального порога: вместо setFixedSize используйте setMinimumSize(QSize(300, 200))
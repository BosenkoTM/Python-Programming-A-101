import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton
from PySide6.QtGui import QColor, QPalette

# Тема. Компоновка интерфейса (Layouts).
# Цель. Изучить, как виджеты автоматически распределяют пространство с помощью QVBoxLayout (вертикальный макет), QHBoxLayout (горизонтальный макет) и QGridLayout (сетка).

# Вспомогательный класс для визуализации макетов (заливает область сплошным цветом)
class Color(QWidget):
    def __init__(self, color_name):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color_name))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Сложные компоновки (Layouts)")

        # Создаем главный контейнер
        main_widget = QWidget()

        # Главный макет будет горизонтальным (QHBoxLayout)
        main_layout = QHBoxLayout()

        # Левая часть интерфейса: вертикальный список цветных блоков (QVBoxLayout)
        left_layout = QVBoxLayout()
        left_layout.addWidget(Color("red"))
        left_layout.addWidget(Color("yellow"))
        left_layout.addWidget(Color("purple"))

        # Правая часть интерфейса: Сетка (QGridLayout)
        right_grid = QGridLayout()
        # Добавляем виджеты по координатам (строка, колонка)
        right_grid.addWidget(Color("blue"), 0, 0)
        right_grid.addWidget(Color("green"), 0, 1)
        right_grid.addWidget(Color("orange"), 1, 0)
        right_grid.addWidget(Color("cyan"), 1, 1)

        # Объединяем макеты: добавляем левый вертикальный и правый сеточный макеты в главный
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_grid)

        # Настраиваем отступы внутри макета
        main_layout.setContentsMargins(10, 10, 10, 10)  # Слева, Сверху, Справа, Снизу
        main_layout.setSpacing(15)  # Пространство между элементами

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# Практическое задание:
# Измените параметры QGridLayout так, чтобы виджет blue занимал две строки в высоту (используйте перегрузку метода addWidget(widget, row, col, rowSpan, colSpan)).
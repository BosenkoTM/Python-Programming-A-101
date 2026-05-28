# Тема. Обработка низкоуровневых событий (Events).
# Цель. Изучить механизм переопределения встроенных обработчиков событий Qt для отслеживания движений мыши и контекстного клика .

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMenu
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Интерактивные события мыши")
        self.label = QLabel("Кликните внутри окна или пошевелите мышью")
        self.label.setStyleSheet("font-size: 16px; font-weight: bold;")

        # Включаем постоянное отслеживание мыши (без необходимости удерживать нажатую кнопку)
        self.setMouseTracking(True)

        self.setCentralWidget(self.label)

    # 1. Переопределяем событие нажатия кнопки мыши
    def mousePressEvent(self, event):
        # Определяем, какая именно кнопка была нажата
        if event.button() == event.button().LeftButton:
            self.label.setText("Нажата ЛЕВАЯ кнопка мыши!")
        elif event.button() == event.button().RightButton:
            self.label.setText("Нажата ПРАВАЯ кнопка мыши!")

    # 2. Переопределяем событие движения мыши
    def mouseMoveEvent(self, event):
        # Выводим текущие координаты курсора относительно нашего окна
        self.label.setText(f"Координаты курсора: X={event.position().x():.0f}, Y={event.position().y():.0f}")

    # 3. Переопределяем событие вызова контекстного меню (обычно правый клик)
    def contextMenuEvent(self, event):
        # Создаем локальное меню прямо в точке клика
        context_menu = QMenu(self)

        action_copy = QAction("Копировать данные", self)
        action_paste = QAction("Вставить данные", self)

        context_menu.addAction(action_copy)
        context_menu.addAction(action_paste)

        # Отображаем меню на экране в глобальных координатах курсора
        context_menu.exec(event.globalPos())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# Практическое задание:
# Добавьте в класс метод keyPressEvent(self, event) для отслеживания нажатия клавиш на клавиатуре. Сделайте так, чтобы при нажатии на клавишу Escape приложение автоматически завершало работу (вызывайте self.close()). Проверить код нажатой клавиши можно через условие: if event.key() == Qt.Key.Key_Escape:. (Не забудьте импортировать Qt из PySide6.QtCore).
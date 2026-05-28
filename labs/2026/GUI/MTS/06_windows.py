# Тема. Работа с несколькими окнами (Multi-Window Applications).
# Цель. Научиться открывать новые второстепенные окна из главного приложения и понять механизм удержания ссылки (Garbage Collection), предотвращающий мгновенное закрытие окон.

import sys
from random import randint
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton

# Создаем класс для нашего дополнительного (второго) окна
class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        # Генерируем случайное число, чтобы видеть, что окно создается заново
        self.label = QLabel(f"Это новое окно. ID сессии: {randint(1, 100)}")
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setWindowTitle("Второстепенное окно")
        self.resize(300, 150)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Инициализируем атрибут для хранения ссылки на окно как None
        self.w = None

        self.setWindowTitle("Главное меню управления")
        self.button = QPushButton("Открыть панель настроек")
        self.button.clicked.connect(self.toggle_sub_window)
        self.setCentralWidget(self.button)

    def toggle_sub_window(self):
        # Важно: если не сохранять объект в self.w, Python удалит локальную переменную
        # сразу после завершения метода, и окно исчезнет за долю секунды!
        if self.w is None:
            # Создаем окно, только если оно еще не создано
            self.w = AnotherWindow()
            self.w.show()
            self.button.setText("Скрыть панель настроек")
        else:
            # Если окно уже открыто — закрываем его и очищаем ссылку
            self.w.close()
            self.w = None
            self.button.setText("Открыть панель настроек")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# Практическое задание:
# Сделайте так, чтобы второе окно открывалось не как обычное плавающее, а как модальное окно поверх главного (пользователь не сможет кликать на главное окно, пока не закроет второе). Для этого перед self.w.show() установите значение: self.w.setWindowModality(Qt.WindowModality.ApplicationModal). Не забудьте импортировать Qt из PySide6.QtCore.
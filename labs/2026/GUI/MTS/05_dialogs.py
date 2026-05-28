# Тема. Диалоговые окна (Dialogs).
#Цель. Изучить вызов стандартных системных диалогов: информационных предупреждений (QMessageBox), запроса ввода (QInputDialog) и выбора файлов (QFileDialog).
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QMessageBox, QInputDialog, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Интеграция системных диалогов")

        container = QWidget()
        layout = QVBoxLayout()

        btn1 = QPushButton("Показать предупреждение (QMessageBox)")
        btn1.clicked.connect(self.show_message_box)
        layout.addWidget(btn1)

        btn2 = QPushButton("Запросить имя пользователя (QInputDialog)")
        btn2.clicked.connect(self.get_user_input)
        layout.addWidget(btn2)

        btn3 = QPushButton("Открыть файл (QFileDialog)")
        btn3.clicked.connect(self.open_file_dialog)
        layout.addWidget(btn3)

        container.setLayout(layout)
        self.setCentralWidget(container)

    # 1. Слот для QMessageBox
    def show_message_box(self):
        # Быстрый вызов критического сообщения с кнопками Ok и Cancel
        button = QMessageBox.critical(
            self,
            "Системная ошибка!",
            "Произошел сбой соединения с базой данных.",
            buttons=QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Ignore,
            defaultButton=QMessageBox.StandardButton.Discard
        )
        if button == QMessageBox.StandardButton.Discard:
            print("Пользователь выбрал: Сбросить изменения")

    # 2. Слот для QInputDialog
    def get_user_input(self):
        # Метод запрашивает текст. Возвращает кортеж: (введенная строка, статус нажатия Ok/Cancel)
        text, ok = QInputDialog.getText(self, "Регистрация", "Введите ваше имя:")
        if ok and text:
            print(f"Зарегистрирован пользователь: {text}")

    # 3. Слот для QFileDialog
    def open_file_dialog(self):
        # Открытие окна проводника для выбора файлов формата .txt или .py
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выбрать файл проекта",
            "",
            "Текстовые файлы (*.txt);;Скрипты Python (*.py);;Все файлы (*)"
        )
        if file_path:
            print(f"Выбран файл по пути: {file_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# Практическое задание:
# Перепишите вызов QFileDialog так, чтобы пользователь мог выбрать не один файл, а сразу несколько файлов одновременно (используйте getOpenFileNames вместо getOpenFileName). Выведите список всех выбранных файлов в консоль.

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QCheckBox, QComboBox, QLineEdit
from PySide6.QtCore import Qt

# Тема. Основные интерактивные элементы управления (Widgets).
# Цель. Изучить поведение текстовых меток (QLabel), чекбоксов (QCheckBox), выпадающих списков (QComboBox) и текстовых полей ввода (QLineEdit).
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Изучение базовых виджетов")

        # Так как в окне будет несколько элементов, нам нужен контейнер QWidget и компоновка
        container = QWidget()
        layout = QVBoxLayout()  # Вертикальное расположение элементов

        # --- 1. Текстовая метка (QLabel) ---
        self.label = QLabel("Добро пожаловать в мир Qt6!")
        font = self.label.font()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter) # Выравнивание по центру
        layout.addWidget(self.label)

        # --- 2. Флажок (QCheckBox) ---
        self.checkbox = QCheckBox("Я согласен с условиями лицензии")
        self.checkbox.stateChanged.connect(self.checkbox_state_changed)
        layout.addWidget(self.checkbox)

        # --- 3. Выпадающий список (QComboBox) ---
        self.combo = QComboBox()
        self.combo.addItems(["Москва", "Санкт-Петербург", "Новосибирск"])
        # Сигнал изменения выбранного элемента
        self.combo.currentIndexChanged.connect(self.combo_index_changed)
        layout.addWidget(self.combo)

        # --- 4. Текстовое поле ввода (QLineEdit) ---
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Введите ваше имя здесь...")
        # Сигнал отправляется, когда пользователь ввел текст и нажал Enter
        self.line_edit.returnPressed.connect(self.line_edit_submitted)
        layout.addWidget(self.line_edit)

        # Устанавливаем макет для нашего контейнера, а контейнер — в окно
        container.setLayout(layout)
        self.setCentralWidget(container)

    # Слоты для обработки событий
    def checkbox_state_changed(self, state):
        # Состояние возвращается в виде чисел (0 - Unchecked, 2 - Checked)
        if state == 2:
            self.label.setText("Лицензия принята!")
        else:
            self.label.setText("Лицензия отклонена.")

    def combo_index_changed(self, index):
        city = self.combo.itemText(index)
        self.label.setText(f"Выбран город: {city}")

    def line_edit_submitted(self):
        text = self.line_edit.text()
        self.label.setText(f"Привет, {text}!")
        self.line_edit.clear() # Очищаем поле ввода после отправки

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# Практическое задание:
# Разрешите пользователю редактировать значения в QComboBox (добавлять свои города), применив метод self.combo.setEditable(True).
# Ограничьте ввод в поле QLineEdit максимум до 10 символов с помощью setMaxLength(10).
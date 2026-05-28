

# Тема. Панели инструментов, меню и действия (Actions, Toolbars & Menus).
# Цель. Создать классическую архитектуру настольного приложения с системным меню, кнопками на панели инструментов и динамической строкой состояния (StatusBar)

import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Приложение с Меню и Панелью инструментов")

        # Центральный виджет для демонстрации работы
        self.label = QLabel("Выберите действие из панели инструментов или меню")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)

        # --- 1. Создание строки состояния (StatusBar) ---
        self.setStatusBar(QStatusBar(self))

        # --- 2. Создание Действия (QAction) ---
        # Действия объединяют функционал, который может быть вызван и через кнопку, и через меню
        self.button_action = QAction("&Новый файл", self)
        self.button_action.setStatusTip("Создать новый рабочий документ")  # Текст подсказки в StatusBar
        self.button_action.triggered.connect(self.on_my_action_triggered)

        # Добавление быстрой комбинации клавиш (Shortcut)
        self.button_action.setShortcut(QKeySequence("Ctrl+N"))

        # Добавим иконку (если есть файл, иначе Qt проигнорирует)
        # В реальном проекте используйте абсолютные или относительные пути к PNG
        self.button_action.setIcon(QIcon("new_file_icon.png"))

        # --- 3. Создание Меню (Menu Bar) ---
        menu = self.menuBar()
        file_menu = menu.addMenu("&Файл")
        file_menu.addAction(self.button_action)  # Добавляем действие в меню

        # Добавляем разделитель и действие выхода
        file_menu.addSeparator()
        exit_action = QAction("&Выход", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # --- 4. Панель инструментов (Toolbar) ---
        toolbar = QToolBar("Главная панель инструментов")
        self.addToolBar(toolbar)
        toolbar.addAction(self.button_action)  # Добавляем то же действие на панель инструментов

    def on_my_action_triggered(self):
        self.label.setText("Сработало действие: 'Новый файл'!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# Практическое задание:
# Добавьте второе действие «Сохранить» (с шорткатом Ctrl+S), разместите его в меню «Файл» и на панели инструментов. При его вызове текст метки должен меняться на «Файл успешно сохранен!».
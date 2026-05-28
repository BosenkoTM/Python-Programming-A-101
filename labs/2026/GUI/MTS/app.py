"""
GUI-приложение "Линейка тарифов оператора связи".
Вариант 30. Демонстрация подключения tkinter к модели ООП из прошлого занятия.

Архитектура:
    - tariff_model.py (концептуально) — классы Tariff, FamilyTariff, Operator.
      Здесь они вставлены в начало файла для простоты запуска одним скриптом.
    - TariffApp (этот файл) — слой представления.

Принципы:
    * Модель НЕ знает о tkinter — её можно использовать в любом другом UI.
    * Каждый обработчик кнопки вызывает метод модели и помещает результат
      в соответствующий виджет; ошибки модели ловятся и показываются
      через messagebox.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Optional


# =====================================================================
# === МОДЕЛЬ (повторяет код из прошлого занятия — БЕЗ ИЗМЕНЕНИЙ) =====
# =====================================================================

class Tariff:
    def __init__(self, name, monthly_fee, minutes, gigabytes):
        self.name = name
        self.monthly_fee = monthly_fee
        self.minutes = minutes
        self.gigabytes = gigabytes

    @property
    def name(self): return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Название тарифа должно быть строкой.")
        if not value.strip():
            raise ValueError("Название тарифа не может быть пустым.")
        self._name = value.strip()

    @property
    def monthly_fee(self): return self._monthly_fee
    @monthly_fee.setter
    def monthly_fee(self, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Абонентская плата должна быть числом.")
        if value < 0:
            raise ValueError("Абонентская плата не может быть отрицательной.")
        self._monthly_fee = float(value)

    @property
    def minutes(self): return self._minutes
    @minutes.setter
    def minutes(self, value):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("Количество минут должно быть целым числом.")
        if value < 0:
            raise ValueError("Количество минут не может быть отрицательным.")
        self._minutes = value

    @property
    def gigabytes(self): return self._gigabytes
    @gigabytes.setter
    def gigabytes(self, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Количество ГБ должно быть числом.")
        if value < 0:
            raise ValueError("Количество ГБ не может быть отрицательным.")
        self._gigabytes = float(value)

    def effective_fee(self):
        return self._monthly_fee

    def kind(self):
        # Для GUI-таблицы — короткая метка типа тарифа.
        return "обычный"

    def __str__(self):
        return (f"{self._name}: {self._monthly_fee:.0f} ₽/мес, "
                f"{self._minutes} мин, {self._gigabytes:g} ГБ")


class FamilyTariff(Tariff):
    def __init__(self, name, monthly_fee, minutes, gigabytes,
                 numbers_count, discount):
        super().__init__(name, monthly_fee, minutes, gigabytes)
        self.numbers_count = numbers_count
        self.discount = discount

    @property
    def numbers_count(self): return self._numbers_count
    @numbers_count.setter
    def numbers_count(self, value):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("Количество номеров должно быть целым числом.")
        if value < 2:
            raise ValueError("Семейный тариф требует минимум 2 номера.")
        self._numbers_count = value

    @property
    def discount(self): return self._discount
    @discount.setter
    def discount(self, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Скидка должна быть числом.")
        if not (0 <= value <= 100):
            raise ValueError("Скидка должна быть в диапазоне [0, 100] %.")
        self._discount = float(value)

    def effective_fee(self):
        total = self._monthly_fee * self._numbers_count
        return total * (1 - self._discount / 100)

    def kind(self):
        return "семейный"

    def __str__(self):
        return (f"{self._name} (семейный, {self._numbers_count} ном., "
                f"−{self._discount:g}%): итого {self.effective_fee():.0f} ₽/мес")


class Operator:
    def __init__(self):
        self._tariffs = []

    def add_tariff(self, tariff):
        if not isinstance(tariff, Tariff):
            raise TypeError("Можно добавлять только объекты Tariff или его наследников.")
        if any(t.name.lower() == tariff.name.lower() for t in self._tariffs):
            raise ValueError(f"Тариф с названием '{tariff.name}' уже существует.")
        self._tariffs.append(tariff)

    def remove_tariff(self, name):
        if not isinstance(name, str):
            raise TypeError("Имя тарифа должно быть строкой.")
        for i, t in enumerate(self._tariffs):
            if t.name.lower() == name.lower():
                return self._tariffs.pop(i)
        raise ValueError(f"Тариф '{name}' не найден.")

    def find_tariff(self, name):
        if not isinstance(name, str):
            raise TypeError("Имя тарифа должно быть строкой.")
        for t in self._tariffs:
            if t.name.lower() == name.lower():
                return t
        return None

    def affordable(self, max_fee):
        if isinstance(max_fee, bool) or not isinstance(max_fee, (int, float)):
            raise TypeError("Порог стоимости должен быть числом.")
        if max_fee < 0:
            raise ValueError("Порог стоимости не может быть отрицательным.")
        return [t for t in self._tariffs if t.effective_fee() <= max_fee]

    def sorted_by_price(self, descending=False):
        return sorted(self._tariffs,
                      key=lambda t: t.effective_fee(),
                      reverse=descending)

    def summary(self):
        count = len(self._tariffs)
        if count == 0:
            return {"count": 0, "avg_gigabytes": 0.0,
                    "avg_fee": 0.0, "min_fee": None, "max_fee": None}
        fees = [t.effective_fee() for t in self._tariffs]
        gbs = [t.gigabytes for t in self._tariffs]
        return {
            "count": count,
            "avg_gigabytes": sum(gbs) / count,
            "avg_fee": sum(fees) / count,
            "min_fee": min(fees),
            "max_fee": max(fees),
        }

    def __len__(self):
        return len(self._tariffs)

    def __iter__(self):
        return iter(self._tariffs)


# =====================================================================
# === ДИАЛОГ ДОБАВЛЕНИЯ ТАРИФА ========================================
# =====================================================================

class AddTariffDialog(tk.Toplevel):
    """
    Модальное окно для ввода данных нового тарифа.
    Возвращает созданный объект в self.result или None при отмене.
    """

    def __init__(self, master):
        super().__init__(master)
        self.title("Новый тариф")
        self.resizable(False, False)
        self.result: Optional[Tariff] = None

        # Группа полей — общие для обоих типов тарифа.
        frm = ttk.Frame(self, padding=12)
        frm.pack(fill="both", expand=True)

        # tk-переменные для удобной работы с виджетами.
        self.var_name = tk.StringVar()
        self.var_fee = tk.StringVar()
        self.var_min = tk.StringVar()
        self.var_gb = tk.StringVar()
        self.var_is_family = tk.BooleanVar(value=False)
        self.var_numbers = tk.StringVar(value="2")
        self.var_discount = tk.StringVar(value="0")

        # Раскладка полей: подпись + поле, по строке на пару.
        rows = [
            ("Название:", self.var_name),
            ("Абон. плата (₽):", self.var_fee),
            ("Минут в пакете:", self.var_min),
            ("ГБ в пакете:", self.var_gb),
        ]
        for i, (label, var) in enumerate(rows):
            ttk.Label(frm, text=label).grid(row=i, column=0, sticky="e",
                                            padx=(0, 8), pady=3)
            ttk.Entry(frm, textvariable=var, width=22).grid(row=i, column=1,
                                                            sticky="we", pady=3)

        # Чекбокс «Семейный» включает дополнительные поля.
        ttk.Separator(frm, orient="horizontal").grid(row=4, column=0,
                                                     columnspan=2, sticky="we",
                                                     pady=8)
        ttk.Checkbutton(frm, text="Семейный тариф",
                        variable=self.var_is_family,
                        command=self._toggle_family_fields).grid(
            row=5, column=0, columnspan=2, sticky="w")

        ttk.Label(frm, text="Кол-во номеров:").grid(row=6, column=0, sticky="e",
                                                    padx=(0, 8), pady=3)
        self.entry_numbers = ttk.Entry(frm, textvariable=self.var_numbers,
                                       width=22)
        self.entry_numbers.grid(row=6, column=1, sticky="we", pady=3)

        ttk.Label(frm, text="Скидка (%):").grid(row=7, column=0, sticky="e",
                                                 padx=(0, 8), pady=3)
        self.entry_discount = ttk.Entry(frm, textvariable=self.var_discount,
                                        width=22)
        self.entry_discount.grid(row=7, column=1, sticky="we", pady=3)

        # Кнопки OK / Отмена.
        btns = ttk.Frame(frm)
        btns.grid(row=8, column=0, columnspan=2, pady=(12, 0))
        ttk.Button(btns, text="Добавить", command=self._on_ok).pack(
            side="left", padx=4)
        ttk.Button(btns, text="Отмена", command=self._on_cancel).pack(
            side="left", padx=4)

        # Начальное состояние «семейных» полей — выключены.
        self._toggle_family_fields()

        # Делаем окно модальным: блокируем главное окно, ждём закрытия.
        self.transient(master)
        self.grab_set()
        self.bind("<Return>", lambda e: self._on_ok())
        self.bind("<Escape>", lambda e: self._on_cancel())
        self.var_name and self.after(50, self._focus_first)

    def _focus_first(self):
        # Чтобы курсор сразу стоял в первом поле — удобство для пользователя.
        for w in self.winfo_children():
            if isinstance(w, ttk.Frame):
                for child in w.winfo_children():
                    if isinstance(child, ttk.Entry):
                        child.focus_set()
                        return

    def _toggle_family_fields(self):
        # Серое неактивное состояние полей, если тариф не семейный.
        state = "normal" if self.var_is_family.get() else "disabled"
        self.entry_numbers.configure(state=state)
        self.entry_discount.configure(state=state)

    def _parse_float(self, raw, field):
        """Универсальный разбор числового поля; единый стиль сообщений об ошибке."""
        s = raw.strip().replace(",", ".")
        if not s:
            raise ValueError(f"Поле «{field}» не заполнено.")
        try:
            return float(s)
        except ValueError:
            raise ValueError(f"Поле «{field}» должно быть числом.")

    def _parse_int(self, raw, field):
        s = raw.strip()
        if not s:
            raise ValueError(f"Поле «{field}» не заполнено.")
        try:
            return int(s)
        except ValueError:
            raise ValueError(f"Поле «{field}» должно быть целым числом.")

    def _on_ok(self):
        """
        Собираем объект тарифа. Исключения модели (TypeError / ValueError)
        ловим и показываем как messagebox, окно не закрываем — даём
        пользователю исправить ввод.
        """
        try:
            name = self.var_name.get().strip()
            fee = self._parse_float(self.var_fee.get(), "Абон. плата")
            minutes = self._parse_int(self.var_min.get(), "Минут в пакете")
            gb = self._parse_float(self.var_gb.get(), "ГБ в пакете")

            if self.var_is_family.get():
                numbers = self._parse_int(self.var_numbers.get(),
                                          "Кол-во номеров")
                discount = self._parse_float(self.var_discount.get(),
                                             "Скидка")
                tariff = FamilyTariff(name, fee, minutes, gb,
                                      numbers, discount)
            else:
                tariff = Tariff(name, fee, minutes, gb)

        except (TypeError, ValueError) as e:
            messagebox.showerror("Ошибка ввода", str(e), parent=self)
            return

        self.result = tariff
        self.destroy()

    def _on_cancel(self):
        self.result = None
        self.destroy()


# =====================================================================
# === ГЛАВНОЕ ОКНО ====================================================
# =====================================================================

class TariffApp(tk.Tk):
    """
    Главное окно приложения. Содержит:
      - таблицу тарифов (Treeview)
      - панель кнопок управления
      - поле поиска
      - фильтр по максимальной цене
      - панель сводной статистики
    """

    def __init__(self):
        super().__init__()
        self.title("Линейка тарифов — Оператор связи (Вариант 30)")
        self.geometry("820x560")
        self.minsize(700, 480)

        # Единственный экземпляр модели на всё приложение.
        self.operator = Operator()
        # Текущий порядок сортировки колонки «Эфф. цена».
        self._sort_desc = False

        self._build_ui()
        self._load_demo_data()
        self._refresh_table()

    # ----- Построение интерфейса ---------------------------------------
    def _build_ui(self):
        # Верхняя панель — кнопки управления.
        top = ttk.Frame(self, padding=(10, 10, 10, 5))
        top.pack(fill="x")

        ttk.Button(top, text="➕ Добавить тариф",
                   command=self._on_add).pack(side="left", padx=4)
        ttk.Button(top, text="🗑 Удалить выбранный",
                   command=self._on_remove).pack(side="left", padx=4)
        ttk.Button(top, text="↕ Сортировать по цене",
                   command=self._on_sort).pack(side="left", padx=4)
        ttk.Button(top, text="🔄 Сбросить фильтры",
                   command=self._refresh_table).pack(side="left", padx=4)

        # Панель поиска и фильтра.
        search = ttk.Frame(self, padding=(10, 0, 10, 5))
        search.pack(fill="x")

        ttk.Label(search, text="Поиск по названию:").pack(side="left")
        self.var_search = tk.StringVar()
        ttk.Entry(search, textvariable=self.var_search,
                  width=20).pack(side="left", padx=(4, 8))
        ttk.Button(search, text="Найти",
                   command=self._on_find).pack(side="left")

        ttk.Separator(search, orient="vertical").pack(side="left",
                                                      fill="y", padx=12)

        ttk.Label(search, text="Макс. цена (₽):").pack(side="left")
        self.var_max_fee = tk.StringVar()
        ttk.Entry(search, textvariable=self.var_max_fee,
                  width=10).pack(side="left", padx=(4, 8))
        ttk.Button(search, text="Применить фильтр",
                   command=self._on_filter).pack(side="left")

        # Таблица тарифов — Treeview.
        table_frame = ttk.Frame(self, padding=(10, 5))
        table_frame.pack(fill="both", expand=True)

        columns = ("name", "kind", "fee", "minutes", "gb", "effective")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings",
                                 height=12)

        headings = [
            ("name",      "Название",    180, "w"),
            ("kind",      "Тип",         100, "w"),
            ("fee",       "Абонплата",   100, "e"),
            ("minutes",   "Минуты",       80, "e"),
            ("gb",        "ГБ",           70, "e"),
            ("effective", "Эфф. цена",   110, "e"),
        ]
        for col, title, width, anchor in headings:
            self.tree.heading(col, text=title)
            self.tree.column(col, width=width, anchor=anchor)

        # Полоса прокрутки для таблицы.
        scroll = ttk.Scrollbar(table_frame, orient="vertical",
                               command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        # Подсветка строки семейного тарифа другим цветом.
        self.tree.tag_configure("family", background="#eef6ff")

        # Нижняя панель — статистика.
        self.summary_var = tk.StringVar(value="—")
        bottom = ttk.Frame(self, padding=(10, 5, 10, 10))
        bottom.pack(fill="x")
        ttk.Label(bottom, text="Сводка:", font=("Arial", 10, "bold")).pack(
            side="left")
        ttk.Label(bottom, textvariable=self.summary_var).pack(side="left",
                                                               padx=(8, 0))

    # ----- Заполнение начальными данными ---------------------------------
    def _load_demo_data(self):
        """7 тарифов из примера, чтобы было что показать сразу при запуске."""
        demo = [
            Tariff("Старт",     300,  100,  5),
            Tariff("Стандарт",  500,  400, 15),
            Tariff("Премиум",   900, 2000, 50),
            Tariff("Безлимит", 1500, 5000, 200),
            Tariff("Молодёжный", 250, 200, 10),
            FamilyTariff("Семейный Базовый", 400, 500, 20,
                         numbers_count=3, discount=10),
            FamilyTariff("Семейный Премиум", 800, 1500, 60,
                         numbers_count=4, discount=15),
        ]
        for t in demo:
            self.operator.add_tariff(t)

    # ----- Обновление таблицы и статистики -------------------------------
    def _refresh_table(self, items=None):
        """
        Перерисовать таблицу. Если items=None — берём всю линейку
        в текущем порядке сортировки. Иначе показываем переданный список
        (результат поиска / фильтра).
        """
        # Очищаем таблицу.
        self.tree.delete(*self.tree.get_children())

        if items is None:
            items = self.operator.sorted_by_price(descending=self._sort_desc)

        # Заполняем строки. Семейные подсвечиваем тегом.
        for t in items:
            tag = "family" if isinstance(t, FamilyTariff) else ""
            self.tree.insert(
                "", "end",
                values=(t.name, t.kind(),
                        f"{t.monthly_fee:.0f}",
                        t.minutes,
                        f"{t.gigabytes:g}",
                        f"{t.effective_fee():.0f}"),
                tags=(tag,) if tag else ()
            )

        # Сводка обновляется всегда по полной линейке, а не по фильтру —
        # иначе пользователь потеряет общую картину.
        self._update_summary()

    def _update_summary(self):
        s = self.operator.summary()
        if s["count"] == 0:
            self.summary_var.set("линейка пуста")
            return
        self.summary_var.set(
            f"всего {s['count']} тарифов  |  "
            f"средняя плата: {s['avg_fee']:.0f} ₽  |  "
            f"среднее ГБ: {s['avg_gigabytes']:.1f}  |  "
            f"минимум: {s['min_fee']:.0f} ₽  |  "
            f"максимум: {s['max_fee']:.0f} ₽"
        )

    # ----- Обработчики кнопок --------------------------------------------
    def _on_add(self):
        dlg = AddTariffDialog(self)
        self.wait_window(dlg)
        if dlg.result is None:
            return
        try:
            self.operator.add_tariff(dlg.result)
        except (TypeError, ValueError) as e:
            messagebox.showerror("Не удалось добавить", str(e))
            return
        self._refresh_table()
        messagebox.showinfo("Готово", f"Тариф «{dlg.result.name}» добавлен.")

    def _on_remove(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Удаление",
                                    "Сначала выберите тариф в таблице.")
            return
        name = self.tree.item(sel[0], "values")[0]
        if not messagebox.askyesno("Подтверждение",
                                    f"Удалить тариф «{name}» из линейки?"):
            return
        try:
            self.operator.remove_tariff(name)
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
            return
        self._refresh_table()

    def _on_find(self):
        query = self.var_search.get().strip()
        if not query:
            messagebox.showinfo("Поиск",
                                 "Введите название тарифа для поиска.")
            return
        try:
            found = self.operator.find_tariff(query)
        except TypeError as e:
            messagebox.showerror("Ошибка поиска", str(e))
            return
        if found is None:
            messagebox.showinfo("Поиск",
                                 f"Тариф «{query}» не найден.")
            return
        # Подсветим найденную строку в таблице (восстановив полный список).
        self._refresh_table()
        for item_id in self.tree.get_children():
            if self.tree.item(item_id, "values")[0].lower() == found.name.lower():
                self.tree.selection_set(item_id)
                self.tree.focus(item_id)
                self.tree.see(item_id)
                break

    def _on_filter(self):
        raw = self.var_max_fee.get().strip().replace(",", ".")
        if not raw:
            messagebox.showinfo("Фильтр",
                                 "Введите максимальную цену для фильтрации.")
            return
        try:
            max_fee = float(raw)
        except ValueError:
            messagebox.showerror("Ошибка", "Цена должна быть числом.")
            return
        try:
            items = self.operator.affordable(max_fee)
        except (TypeError, ValueError) as e:
            messagebox.showerror("Ошибка", str(e))
            return
        if not items:
            messagebox.showinfo("Фильтр",
                                 f"Нет тарифов дешевле {max_fee:.0f} ₽.")
            self._refresh_table([])
            return
        self._refresh_table(items)

    def _on_sort(self):
        # Каждый клик переключает направление сортировки.
        self._sort_desc = not self._sort_desc
        self._refresh_table()


# =====================================================================
# === ТОЧКА ВХОДА =====================================================
# =====================================================================
if __name__ == "__main__":
    app = TariffApp()
    app.mainloop()

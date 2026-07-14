import tkinter as tk

from tkinter import (
    messagebox,
    filedialog
)


# Информационное окно

class AboutDialog:
    #Окно "О программе".


    def __init__(self, parent):

        self.window = tk.Toplevel(
            parent
        )

        self.window.title(
            "О программе"
        )

        self.window.geometry(
            "350x250"
        )


        text = """
Pomodoro Timer with Analytics

Версия: 1.0

Возможности:

• Таймер Pomodoro
• Логирование сессий
• Анализ продуктивности
• Статистика
• Экспорт данных
"""


        label = tk.Label(
            self.window,
            text=text,
            justify="left"
        )

        label.pack(
            padx=20,
            pady=20
        )


        tk.Button(
            self.window,
            text="Закрыть",
            command=self.window.destroy
        ).pack()


# Подтверждение действия

class ConfirmDialog:
    Диалог подтверждения.


    @staticmethod
    def ask(
            title,
            message
    ):

        return messagebox.askyesno(
            title,
            message
        )


# Ошибка

class ErrorDialog:
    #Отображение ошибки.


    @staticmethod
    def show(
            message
    ):

        messagebox.showerror(
            "Ошибка",
            message
        )


# Информация

class InfoDialog:
    #Информационное сообщение.


    @staticmethod
    def show(
            message
    ):

        messagebox.showinfo(
            "Информация",
            message
        )


# Настройки Pomodoro

class SettingsDialog:
    #Отдельное окно настройки времени.


    def __init__(
            self,
            parent,
            current_settings,
            save_callback
    ):

        self.save_callback = save_callback


        self.window = tk.Toplevel(
            parent
        )

        self.window.title(
            "Настройки Pomodoro"
        )

        self.window.geometry(
            "300x250"
        )


        # Поля ввода


        tk.Label(
            self.window,
            text="Рабочий интервал:"
        ).pack()


        self.work_entry = tk.Entry(
            self.window
        )

        self.work_entry.insert(
            0,
            current_settings.get(
                "work_time",
                25
            )
        )

        self.work_entry.pack()



        tk.Label(
            self.window,
            text="Короткий отдых:"
        ).pack()


        self.short_entry = tk.Entry(
            self.window
        )


        self.short_entry.insert(
            0,
            current_settings.get(
                "short_break",
                5
            )
        )


        self.short_entry.pack()



        tk.Label(
            self.window,
            text="Длинный отдых:"
        ).pack()


        self.long_entry = tk.Entry(
            self.window
        )


        self.long_entry.insert(
            0,
            current_settings.get(
                "long_break",
                15
            )
        )


        self.long_entry.pack()



        tk.Button(
            self.window,
            text="Сохранить",
            command=self.save
        ).pack(
            pady=10
        )



    def save(self):
        #Сохранение настроек.

        try:

            settings = {

                "work_time":
                    int(
                        self.work_entry.get()
                    ),

                "short_break":
                    int(
                        self.short_entry.get()
                    ),

                "long_break":
                    int(
                        self.long_entry.get()
                    )

            }


            self.save_callback(
                settings
            )


            self.window.destroy()



        except ValueError:

            ErrorDialog.show(
                "Введите числовые значения"
            )


# Выбор файла экспорта

class ExportDialog:
    #Окно выбора места сохранения.


    @staticmethod
    def choose_file():

        return filedialog.asksaveasfilename(

            title="Сохранить экспорт",

            defaultextension=".json",

            filetypes=[

                (
                    "CSV файлы",
                    "*.csv"
                ),

                (
                    "JSON файлы",
                    "*.json"
                )

            ]

        )

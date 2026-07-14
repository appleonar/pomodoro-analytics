import tkinter as tk
from tkinter import messagebox

from datetime import datetime

from core.timer import PomodoroTimer
from core.storage import Storage
from core.statistics import StatisticsManager
from core.export import SessionExporter

from config import (
    WINDOW_TITLE,
    WINDOW_SIZE
)


class MainWindow:
    #Главное окно приложения.


    def __init__(self, root):

        self.root = root

        self.root.title(
            WINDOW_TITLE
        )

        self.root.geometry(
            WINDOW_SIZE
        )


        # Подключение модулей

        self.timer = PomodoroTimer()

        self.storage = Storage()

        self.exporter = SessionExporter()


        # состояние интерфейса

        self.timer_job = None


        # создание интерфейса

        self.create_widgets()


    # Создание элементов интерфейса

    def create_widgets(self):



        # Таймер

        self.timer_label = tk.Label(
            self.root,
            text="25:00",
            font=("Arial", 40)
        )

        self.timer_label.pack(
            pady=20
        )


        self.session_label = tk.Label(
            self.root,
            text="Работа",
            font=("Arial", 16)
        )

        self.session_label.pack()



        # Кнопки управления

        buttons_frame = tk.Frame(
            self.root
        )

        buttons_frame.pack(
            pady=20
        )


        self.start_button = tk.Button(
            buttons_frame,
            text="Старт",
            width=12,
            command=self.start_timer
        )

        self.start_button.grid(
            row=0,
            column=0,
            padx=5
        )



        self.pause_button = tk.Button(
            buttons_frame,
            text="Пауза",
            width=12,
            command=self.pause_timer
        )

        self.pause_button.grid(
            row=0,
            column=1,
            padx=5
        )



        self.reset_button = tk.Button(
            buttons_frame,
            text="Сброс",
            width=12,
            command=self.reset_timer
        )

        self.reset_button.grid(
            row=0,
            column=2,
            padx=5
        )



        # Настройки времени

        settings_frame = tk.LabelFrame(
            self.root,
            text="Настройки"
        )

        settings_frame.pack(
            pady=10
        )


        tk.Label(
            settings_frame,
            text="Работа:"
        ).grid(
            row=0,
            column=0
        )


        self.work_entry = tk.Entry(
            settings_frame,
            width=5
        )

        self.work_entry.insert(
            0,
            "25"
        )

        self.work_entry.grid(
            row=0,
            column=1
        )



        tk.Label(
            settings_frame,
            text="Отдых:"
        ).grid(
            row=1,
            column=0
        )


        self.break_entry = tk.Entry(
            settings_frame,
            width=5
        )

        self.break_entry.insert(
            0,
            "5"
        )

        self.break_entry.grid(
            row=1,
            column=1
        )



        tk.Button(
            settings_frame,
            text="Сохранить",
            command=self.save_settings
        ).grid(
            row=2,
            column=0,
            columnspan=2,
            pady=5
        )



        # Статистика

        statistics_frame = tk.LabelFrame(
            self.root,
            text="Статистика"
        )

        statistics_frame.pack(
            pady=15
        )


        self.statistics_label = tk.Label(
            statistics_frame,
            text="Нет данных",
            justify="left"
        )

        self.statistics_label.pack(
            padx=20,
            pady=10
        )


        tk.Button(
            self.root,
            text="Обновить статистику",
            command=self.show_statistics
        ).pack()



        # Экспорт

        tk.Button(
            self.root,
            text="Экспорт CSV",
            command=self.export_csv
        ).pack(
            pady=10
        )



    # Таймер


    def start_timer(self):

        self.timer.start()

        self.update_timer()



    def update_timer(self):

        if self.timer.running:

            finished = self.timer.tick()


            self.timer_label.config(
                text=self.timer.get_time()
            )


            if finished:

                self.save_completed_session()


                messagebox.showinfo(
                    "Pomodoro",
                    "Сессия завершена!"
                )


                self.session_label.config(
                    text=self.timer.get_session_type()
                )


            self.timer_job = self.root.after(
                1000,
                self.update_timer
            )



    def pause_timer(self):

        self.timer.pause()



    def reset_timer(self):

        self.timer.reset()

        self.timer_label.config(
            text=self.timer.get_time()
        )



    # Настройки

    def save_settings(self):

        try:

            work = int(
                self.work_entry.get()
            )

            short_break = int(
                self.break_entry.get()
            )


            self.timer.set_times(
                work,
                short_break,
                self.timer.long_break
            )


            self.storage.save_settings({

                "work_time": work,

                "short_break": short_break,

                "long_break":
                    self.timer.long_break

            })


            messagebox.showinfo(
                "Настройки",
                "Настройки сохранены"
            )


        except ValueError:

            messagebox.showerror(
                "Ошибка",
                "Введите числа"
            )


    # Сохранение сессии

    def save_completed_session(self):


        now = datetime.now()


        session = {

            "date":
                now.strftime(
                    "%Y-%m-%d"
                ),

            "start_time":
                now.strftime(
                    "%H:%M:%S"
                ),

            "end_time":
                now.strftime(
                    "%H:%M:%S"
                ),

            "duration":
                self.timer.work_time,

            "session_type":
                "work",

            "completed":
                True,

            "weekday":
                now.strftime(
                    "%A"
                )

        }


        self.storage.add_session(
            session
        )



    # Статистика

    def show_statistics(self):

        sessions = (
            self.storage.load_sessions()
        )


        stats = StatisticsManager(
            sessions
        )


        data = (
            stats.full_statistics()
        )


        text = f"""
Сегодня:
{data['today']}

Неделя:
{data['week']}

Лучший час:
{data['productivity']['best_hour']}

Лучший день:
{data['productivity']['best_day']}
"""


        self.statistics_label.config(
            text=text
        )



    # Экспорт

    def export_csv(self):

        sessions = (
            self.storage.load_sessions()
        )


        file = self.exporter.export_csv(
            sessions
        )


        messagebox.showinfo(
            "Экспорт",
            f"Файл создан:\n{file}"
        )

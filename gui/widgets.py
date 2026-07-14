import tkinter as tk


# Таймер

class TimerLabel(tk.Label):
    #Большое поле отображения времени.



    def __init__(self, parent):

        super().__init__(
            parent,
            text="25:00",
            font=("Arial", 40)
        )


    def update_time(self, value):
        #Обновление отображаемого времени.


        self.config(
            text=value
        )



# Название текущей сессии

class SessionTypeLabel(tk.Label):
    #Отображает тип текущего режима: Работа / Отдых.


    def __init__(self, parent):

        super().__init__(
            parent,
            text="Работа",
            font=("Arial", 16)
        )


    def update_type(self, value):

        self.config(
            text=value
        )


# Панель кнопок управления

class TimerButtonsFrame(tk.Frame):
    #Панель управления таймером.


    def __init__(
            self,
            parent,
            start_command,
            pause_command,
            reset_command
    ):

        super().__init__(
            parent
        )


        self.start_button = tk.Button(
            self,
            text="Старт",
            width=12,
            command=start_command
        )


        self.start_button.grid(
            row=0,
            column=0,
            padx=5
        )


        self.pause_button = tk.Button(
            self,
            text="Пауза",
            width=12,
            command=pause_command
        )


        self.pause_button.grid(
            row=0,
            column=1,
            padx=5
        )


        self.reset_button = tk.Button(
            self,
            text="Сброс",
            width=12,
            command=reset_command
        )


        self.reset_button.grid(
            row=0,
            column=2,
            padx=5
        )



# Настройки времени

class SettingsFrame(tk.LabelFrame):
    #Блок настройки времени Pomodoro.


    def __init__(
            self,
            parent,
            save_command
    ):

        super().__init__(
            parent,
            text="Настройки"
        )


        tk.Label(
            self,
            text="Работа:"
        ).grid(
            row=0,
            column=0
        )


        self.work_entry = tk.Entry(
            self,
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
            self,
            text="Отдых:"
        ).grid(
            row=1,
            column=0
        )


        self.break_entry = tk.Entry(
            self,
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



        self.save_button = tk.Button(
            self,
            text="Сохранить",
            command=save_command
        )


        self.save_button.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=5
        )



    def get_values(self):
        """
        Получение введенных настроек.
        """

        return (

            int(
                self.work_entry.get()
            ),

            int(
                self.break_entry.get()
            )

        )


# Блок статистики

class StatisticsFrame(tk.LabelFrame):
    #Отображение статистики.


    def __init__(
            self,
            parent
    ):

        super().__init__(
            parent,
            text="Статистика"
        )


        self.label = tk.Label(
            self,
            text="Нет данных",
            justify="left"
        )


        self.label.pack(
            padx=20,
            pady=10
        )



    def update_statistics(
            self,
            text
    ):

        self.label.config(
            text=text
        )



# Кнопка экспорта

class ExportButton(tk.Button):
    #Кнопка экспорта данных.


    def __init__(
            self,
            parent,
            command
    ):

        super().__init__(
            parent,
            text="Экспорт CSV",
            command=command
        )

from datetime import datetime
from config import (
    DEFAULT_WORK_TIME,
    DEFAULT_SHORT_BREAK,
    DEFAULT_LONG_BREAK,
    LONG_BREAK_INTERVAL,
)


class PomodoroTimer:
     #Класс таймера Pomodoro.

    def __init__(self):
        # Настройки времени (в минутах)
        self.work_time = DEFAULT_WORK_TIME
        self.short_break = DEFAULT_SHORT_BREAK
        self.long_break = DEFAULT_LONG_BREAK

        # Текущее оставшееся время (в секундах)
        self.remaining_time = self.work_time * 60

        # Тип текущей сессии
        self.session_type = "work"

        # Состояние таймера
        self.running = False
        self.paused = False

        # Количество завершённых рабочих сессий
        self.completed_sessions = 0

        # Время начала текущей сессии
        self.start_datetime = None

    # Управление таймером

    def start(self):
        #Запустить таймер.

        if not self.running:
            self.running = True
            self.paused = False

            if self.start_datetime is None:
                self.start_datetime = datetime.now()

    def pause(self):
        #Поставить таймер на паузу.

        if self.running:
            self.running = False
            self.paused = True

    def resume(self):
        #Продолжить работу таймера.

        if self.paused:
            self.running = True
            self.paused = False

    def reset(self):
        #Сбросить текущую сессию.

        self.running = False
        self.paused = False
        self.start_datetime = None

        if self.session_type == "work":
            self.remaining_time = self.work_time * 60

        elif self.session_type == "short_break":
            self.remaining_time = self.short_break * 60

        else:
            self.remaining_time = self.long_break * 60

    # Обновление таймера

    def tick(self):
        #Вызывается каждую секунду. Возвращает True, если сессия закончилась.

        if not self.running:
            return False

        if self.remaining_time > 0:
            self.remaining_time -= 1

        if self.remaining_time == 0:
            self.finish_session()
            return True

        return False

    # Завершение сессии

    def finish_session(self):
        #Завершить текущую сессию.

        self.running = False

        if self.session_type == "work":

            self.completed_sessions += 1

            if self.completed_sessions % LONG_BREAK_INTERVAL == 0:
                self.session_type = "long_break"
                self.remaining_time = self.long_break * 60

            else:
                self.session_type = "short_break"
                self.remaining_time = self.short_break * 60

        else:

            self.session_type = "work"
            self.remaining_time = self.work_time * 60

        self.start_datetime = None

    # Настройки

    def set_times(
        self,
        work_time,
        short_break,
        long_break,
    ):
        #Изменить продолжительность сессий.

        self.work_time = work_time
        self.short_break = short_break
        self.long_break = long_break

        self.reset()

    # Информация

    def get_time(self):
        #Вернуть оставшееся время.

        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60

        return f"{minutes:02}:{seconds:02}"

    def get_session_type(self):
        #Вернуть тип текущей сессии.

        return self.session_type

    def is_running(self):
        #Работает ли таймер.
        return self.running

    def is_paused(self):
        #Стоит ли таймер на паузе.

        return self.paused

    def get_completed_sessions(self):
        #Количество завершённых рабочих сессий.

        return self.completed_sessions

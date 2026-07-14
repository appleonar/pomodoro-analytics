from collections import defaultdict
from datetime import datetime
from statistics import mean


class ProductivityAnalytics:
    #Класс анализа продуктивности.

    def __init__(self, sessions):
        #sessions - список завершённых Pomodoro-сессий
        
        self.sessions = sessions


    # Анализ по времени суток

    def productivity_by_hour(self):
        #Возвращает количество продуктивных минут для каждого часа дня.

        hours = defaultdict(int)

        for session in self.sessions:

            if not session.get("completed"):
                continue

            start_time = session.get("start_time")

            if start_time:

                hour = datetime.strptime(
                    start_time,
                    "%H:%M:%S"
                ).hour

                hours[hour] += session.get(
                    "duration",
                    0
                )

        return dict(hours)


    # Анализ по дням недели

    def productivity_by_weekday(self):
        #Возвращает продуктивность по дням недели.

        weekdays = defaultdict(int)


        for session in self.sessions:

            if not session.get("completed"):
                continue


            day = session.get(
                "weekday"
            )


            if day:

                weekdays[day] += session.get(
                    "duration",
                    0
                )


        return dict(weekdays)


    # Самый продуктивный час

    def best_hour(self):
        #Определяет час, когда пользователь работает наиболее эффективно.

        data = self.productivity_by_hour()


        if not data:
            return None


        return max(
            data,
            key=data.get
        )



    # Самый продуктивный день

    def best_day(self):
        #Определяет самый продуктивный день недели.

        data = self.productivity_by_weekday()


        if not data:
            return None


        return max(
            data,
            key=data.get
        )



    # Количество сессий

    def total_sessions(self):
        #Возвращает количество завершённых Pomodoro.
        
        return len(
            [
                session
                for session in self.sessions
                if session.get("completed")
            ]
        )



    # Общее время работы

    def total_work_time(self):
        #Возвращает общее количество минут продуктивной работы.

        total = 0


        for session in self.sessions:

            if session.get("completed"):

                total += session.get(
                    "duration",
                    0
                )


        return total



    # Средняя продолжительность

    def average_session_duration(self):
        #Средняя длительность Pomodoro.

        durations = []


        for session in self.sessions:

            if session.get("completed"):

                durations.append(
                    session.get(
                        "duration",
                        0
                    )
                )


        if not durations:
            return 0


        return round(
            mean(durations),
            2
        )


    # Полный отчёт
    
    def generate_report(self):
        #Формирует полный аналитический отчёт.

        return {

            "total_sessions":
                self.total_sessions(),

            "total_minutes":
                self.total_work_time(),

            "average_duration":
                self.average_session_duration(),

            "best_hour":
                self.best_hour(),

            "best_day":
                self.best_day(),

            "productivity_by_hour":
                self.productivity_by_hour(),

            "productivity_by_weekday":
                self.productivity_by_weekday()

        }

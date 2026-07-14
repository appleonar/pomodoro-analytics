from datetime import datetime, timedelta

from core.analytics import ProductivityAnalytics



class StatisticsManager:
    #Формирование статистики Pomodoro.


    def __init__(self, sessions):
        #список всех Pomodoro-сессий


        self.sessions = sessions

        self.analytics = ProductivityAnalytics(
            sessions
        )


    # Статистика за сегодня

    def today_statistics(self):
        #Возвращает статистику за текущий день.
        
        today = datetime.now().strftime(
            "%Y-%m-%d"
        )


        today_sessions = [

            session

            for session in self.sessions

            if session.get("date") == today

        ]


        return self._calculate_basic_stats(
            today_sessions
        )


    # Статистика за неделю

    def week_statistics(self):
        #Возвращает статистику за последние 7 дней.

        current_date = datetime.now()


        week_ago = (
            current_date -
            timedelta(days=7)
        )


        week_sessions = []


        for session in self.sessions:

            date_string = session.get(
                "date"
            )


            if not date_string:
                continue


            session_date = datetime.strptime(
                date_string,
                "%Y-%m-%d"
            )


            if session_date >= week_ago:

                week_sessions.append(
                    session
                )


        return self._calculate_basic_stats(
            week_sessions
        )


    # Статистика за месяц

    def month_statistics(self):
        #Статистика за последние 30 дней.

        current_date = datetime.now()


        month_ago = (
            current_date -
            timedelta(days=30)
        )


        month_sessions = []


        for session in self.sessions:

            date_string = session.get(
                "date"
            )


            if not date_string:
                continue


            session_date = datetime.strptime(
                date_string,
                "%Y-%m-%d"
            )


            if session_date >= month_ago:

                month_sessions.append(
                    session
                )


        return self._calculate_basic_stats(
            month_sessions
        )


# Общая статистика

    def all_time_statistics(self):
        #Статистика за весь период.

        return self._calculate_basic_stats(
            self.sessions
        )


    # Расчет основных показателей

    def _calculate_basic_stats(
            self,
            sessions
    ):
        #Внутренний расчет показателей.

        completed_sessions = [

            session

            for session in sessions

            if session.get(
                "completed"
            )

        ]


        total_sessions = len(
            completed_sessions
        )


        total_minutes = sum(

            session.get(
                "duration",
                0
            )

            for session in completed_sessions

        )


        average_duration = 0


        if total_sessions > 0:

            average_duration = round(
                total_minutes /
                total_sessions,
                2
            )


        return {

            "sessions":
                total_sessions,


            "minutes":
                total_minutes,


            "hours":
                round(
                    total_minutes / 60,
                    2
                ),


            "average_session":
                average_duration

        }



    # Формирование полного отчета

    def full_statistics(self):
        #Полная статистика приложения.

        return {

            "today":
                self.today_statistics(),


            "week":
                self.week_statistics(),


            "month":
                self.month_statistics(),


            "all_time":
                self.all_time_statistics(),


            "productivity":
                self.analytics.generate_report()

        }

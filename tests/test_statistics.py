from datetime import datetime, timedelta

from core.statistics import StatisticsManager



# ==================================================
# Тестовые данные
# ==================================================

def get_test_sessions():

    today = datetime.now()

    today_string = today.strftime(
        "%Y-%m-%d"
    )


    yesterday_string = (
        today -
        timedelta(days=1)
    ).strftime(
        "%Y-%m-%d"
    )


    old_date = (
        today -
        timedelta(days=40)
    ).strftime(
        "%Y-%m-%d"
    )


    return [

        {
            "id": 1,

            "date": today_string,

            "duration": 25,

            "completed": True
        },


        {
            "id": 2,

            "date": today_string,

            "duration": 30,

            "completed": True
        },


        {
            "id": 3,

            "date": yesterday_string,

            "duration": 20,

            "completed": True
        },


        {
            "id": 4,

            "date": old_date,

            "duration": 50,

            "completed": True
        },


        {
            "id": 5,

            "date": today_string,

            "duration": 25,

            "completed": False
        }

    ]



# ==================================================
# Проверка статистики за сегодня
# ==================================================

def test_today_statistics():

    sessions = get_test_sessions()


    statistics = StatisticsManager(
        sessions
    )


    result = (
        statistics.today_statistics()
    )


    assert result["sessions"] == 2

    assert result["minutes"] == 55

    assert result["average_session"] == 27.5



# ==================================================
# Проверка статистики за неделю
# ==================================================

def test_week_statistics():

    sessions = get_test_sessions()


    statistics = StatisticsManager(
        sessions
    )


    result = (
        statistics.week_statistics()
    )


    assert result["sessions"] == 3

    assert result["minutes"] == 75



# ==================================================
# Проверка статистики за месяц
# ==================================================

def test_month_statistics():

    sessions = get_test_sessions()


    statistics = StatisticsManager(
        sessions
    )


    result = (
        statistics.month_statistics()
    )


    assert result["sessions"] == 3

    assert result["minutes"] == 75



# ==================================================
# Проверка общей статистики
# ==================================================

def test_all_time_statistics():

    sessions = get_test_sessions()


    statistics = StatisticsManager(
        sessions
    )


    result = (
        statistics.all_time_statistics()
    )


    assert result["sessions"] == 4

    assert result["minutes"] == 125



# ==================================================
# Проверка расчета часов
# ==================================================

def test_hours_calculation():

    sessions = [

        {
            "date": "2026-07-15",

            "duration": 120,

            "completed": True

        }

    ]


    statistics = StatisticsManager(
        sessions
    )


    result = (
        statistics.all_time_statistics()
    )


    assert result["hours"] == 2



# ==================================================
# Проверка средней длительности
# ==================================================

def test_average_session_duration():

    sessions = [

        {
            "date": "2026-07-15",

            "duration": 25,

            "completed": True
        },


        {
            "date": "2026-07-15",

            "duration": 35,

            "completed": True
        }

    ]


    statistics = StatisticsManager(
        sessions
    )


    result = (
        statistics.all_time_statistics()
    )


    assert result["average_session"] == 30



# ==================================================
# Проверка полного отчета
# ==================================================

def test_full_statistics():

    sessions = get_test_sessions()


    statistics = StatisticsManager(
        sessions
    )


    report = (
        statistics.full_statistics()
    )


    assert "today" in report

    assert "week" in report

    assert "month" in report

    assert "all_time" in report

    assert "productivity" in report

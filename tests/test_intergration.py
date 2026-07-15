import json


from core.timer import PomodoroTimer
from core.storage import Storage
from core.analytics import ProductivityAnalytics
from core.statistics import StatisticsManager
from core.export import SessionExporter



# ==================================================
# Полный сценарий Pomodoro-сессии
# ==================================================

def test_full_pomodoro_workflow(tmp_path):

    # ---------------------------------
    # Создаем хранилище
    # ---------------------------------

    storage = Storage()


    storage.sessions_file = (
        tmp_path / "sessions.json"
    )


    storage.save_sessions([])



    # ---------------------------------
    # Создаем таймер
    # ---------------------------------

    timer = PomodoroTimer()


    timer.start()


    assert timer.running is True



    # имитация завершения Pomodoro

    timer.finish_session()



    assert timer.completed_sessions == 1



    # ---------------------------------
    # Сохраняем результат
    # ---------------------------------

    session = {

        "date":
            "2026-07-15",

        "start_time":
            "10:00:00",

        "end_time":
            "10:25:00",

        "duration":
            25,

        "session_type":
            "work",

        "completed":
            True,

        "weekday":
            "Wednesday"

    }


    storage.add_session(
        session
    )



    # ---------------------------------
    # Проверяем запись
    # ---------------------------------

    sessions = (
        storage.load_sessions()
    )


    assert len(sessions) == 1

    assert sessions[0]["duration"] == 25



# ==================================================
# Аналитика после сохранения данных
# ==================================================

def test_storage_to_analytics_flow(tmp_path):


    storage = Storage()


    storage.sessions_file = (
        tmp_path / "sessions.json"
    )


    storage.save_sessions([

        {

            "id":1,

            "date":
                "2026-07-15",

            "start_time":
                "09:00:00",

            "duration":
                25,

            "completed":
                True,

            "weekday":
                "Wednesday"

        },

        {

            "id":2,

            "date":
                "2026-07-15",

            "start_time":
                "14:00:00",

            "duration":
                50,

            "completed":
                True,

            "weekday":
                "Wednesday"

        }

    ])



    sessions = (
        storage.load_sessions()
    )


    analytics = ProductivityAnalytics(
        sessions
    )


    result = (
        analytics.generate_report()
    )



    assert result["total_sessions"] == 2

    assert result["total_minutes"] == 75

    assert result["best_hour"] == 14



# ==================================================
# Проверка цепочки:
# Storage -> Statistics
# ==================================================

def test_storage_to_statistics_flow(tmp_path):


    storage = Storage()


    storage.sessions_file = (
        tmp_path / "sessions.json"
    )


    storage.save_sessions([

        {

            "id":1,

            "date":
                "2026-07-15",

            "duration":
                25,

            "completed":
                True

        }

    ])



    sessions = (
        storage.load_sessions()
    )



    statistics = StatisticsManager(
        sessions
    )


    result = (
        statistics.all_time_statistics()
    )



    assert result["sessions"] == 1

    assert result["minutes"] == 25

    assert result["hours"] == 0.42



# ==================================================
# Проверка экспорта
# ==================================================

def test_statistics_export_flow(tmp_path):


    exporter = SessionExporter()


    exporter.export_dir = tmp_path



    sessions = [

        {

            "id":1,

            "duration":25,

            "completed":True

        }

    ]



    file = exporter.export_json(
        sessions
    )



    assert file.exists()



    with open(
        file,
        "r",
        encoding="utf-8"
    ) as f:


        data = json.load(
            f
        )


    assert len(data) == 1

    assert data[0]["duration"] == 25



# ==================================================
# Полный путь:
# Timer -> Storage -> Statistics -> Export
# ==================================================

def test_complete_application_flow(tmp_path):


    # Таймер

    timer = PomodoroTimer()


    timer.start()

    timer.finish_session()



    # Хранилище

    storage = Storage()


    storage.sessions_file = (
        tmp_path / "sessions.json"
    )


    storage.save_sessions([])



    storage.add_session({

        "date":
            "2026-07-15",

        "duration":
            25,

        "completed":
            True,

        "weekday":
            "Wednesday",

        "start_time":
            "10:00:00"

    })



    # Статистика

    sessions = (
        storage.load_sessions()
    )


    statistics = StatisticsManager(
        sessions
    )


    report = (
        statistics.full_statistics()
    )



    assert (
        report["all_time"]["sessions"]
        == 1
    )



    # Экспорт

    exporter = SessionExporter()


    exporter.export_dir = tmp_path



    exported = exporter.export_json(
        report
    )


    assert exported.exists()

import pytest

from core.timer import PomodoroTimer



# ==================================================
# Создание таймера
# ==================================================

def test_timer_initial_state():

    timer = PomodoroTimer()


    assert timer.running is False

    assert timer.paused is False

    assert timer.session_type == "work"

    assert timer.remaining_time == (
        timer.work_time * 60
    )



# ==================================================
# Запуск таймера
# ==================================================

def test_start_timer():

    timer = PomodoroTimer()


    timer.start()


    assert timer.running is True

    assert timer.paused is False

    assert timer.start_datetime is not None



# ==================================================
# Пауза
# ==================================================

def test_pause_timer():

    timer = PomodoroTimer()


    timer.start()

    timer.pause()


    assert timer.running is False

    assert timer.paused is True



# ==================================================
# Продолжение после паузы
# ==================================================

def test_resume_timer():

    timer = PomodoroTimer()


    timer.start()

    timer.pause()

    timer.resume()


    assert timer.running is True

    assert timer.paused is False



# ==================================================
# Уменьшение времени
# ==================================================

def test_timer_tick():

    timer = PomodoroTimer()


    timer.start()


    old_time = timer.remaining_time


    timer.tick()


    assert timer.remaining_time == (
        old_time - 1
    )



# ==================================================
# Сброс таймера
# ==================================================

def test_reset_timer():

    timer = PomodoroTimer()


    timer.start()


    timer.tick()

    timer.reset()


    assert timer.running is False

    assert timer.paused is False

    assert timer.remaining_time == (
        timer.work_time * 60
    )



# ==================================================
# Завершение рабочей сессии
# ==================================================

def test_finish_work_session():

    timer = PomodoroTimer()


    timer.finish_session()


    assert timer.session_type == (
        "short_break"
    )

    assert timer.completed_sessions == 1



# ==================================================
# Проверка длинного перерыва
# ==================================================

def test_long_break_after_four_sessions():

    timer = PomodoroTimer()


    timer.completed_sessions = 3

    timer.session_type = "work"


    timer.finish_session()


    assert timer.session_type == (
        "long_break"
    )



# ==================================================
# Формат отображения времени
# ==================================================

def test_get_time_format():

    timer = PomodoroTimer()


    timer.remaining_time = 125


    result = timer.get_time()


    assert result == "02:05"



# ==================================================
# Изменение настроек времени
# ==================================================

def test_set_times():

    timer = PomodoroTimer()


    timer.set_times(
        30,
        10,
        20
    )


    assert timer.work_time == 30

    assert timer.short_break == 10

    assert timer.long_break == 20

    assert timer.remaining_time == (
        30 * 60
    )

from pathlib import Path

# Пути проекта

# Корневая директория проекта
BASE_DIR = Path(__file__).resolve().parent

# Директории
DATA_DIR = BASE_DIR / "data"
EXPORT_DIR = BASE_DIR / "exports"

# Файлы данных
SESSIONS_FILE = DATA_DIR / "sessions.json"
SETTINGS_FILE = DATA_DIR / "settings.json"

# Настройки Pomodoro

# Значения по умолчанию (в минутах)
DEFAULT_WORK_TIME = 25
DEFAULT_SHORT_BREAK = 5
DEFAULT_LONG_BREAK = 15

# Через сколько рабочих сессий начинается длинный отдых
LONG_BREAK_INTERVAL = 4

# Форматы

DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# Интерфейс

WINDOW_TITLE = "Pomodoro Timer with Analytics"

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

WINDOW_SIZE = f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"

# Экспорт

DEFAULT_EXPORT_NAME = "pomodoro_export.csv"

# Создание необходимых папок

DATA_DIR.mkdir(exist_ok=True)
EXPORT_DIR.mkdir(exist_ok=True)

import json
from pathlib import Path

from config import (
    SESSIONS_FILE,
    SETTINGS_FILE,
    DEFAULT_WORK_TIME,
    DEFAULT_SHORT_BREAK,
    DEFAULT_LONG_BREAK,
    LONG_BREAK_INTERVAL
)


class Storage:
    #Класс для работы с файлами данных.
    
    def __init__(self):
        #Создание хранилища.

        self.sessions_file = Path(
            SESSIONS_FILE
        )

        self.settings_file = Path(
            SETTINGS_FILE
        )


        self._create_files()


 # Создание файлов

    def _create_files(self):
        if not self.sessions_file.exists():

            self.save_sessions([])



        if not self.settings_file.exists():

            self.save_settings({

                "work_time":
                    DEFAULT_WORK_TIME,

                "short_break":
                    DEFAULT_SHORT_BREAK,

                "long_break":
                    DEFAULT_LONG_BREAK,

                "long_break_interval":
                    LONG_BREAK_INTERVAL
            })


    # Работа с сессиями

    def load_sessions(self):
        #Загружает список Pomodoro-сессий.


        try:

            with open(
                self.sessions_file,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)


        except (
            json.JSONDecodeError,
            FileNotFoundError
        ):

            return []



    def save_sessions(self, sessions):
        #Сохраняет список сессий.

        with open(
            self.sessions_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                sessions,
                file,
                indent=4,
                ensure_ascii=False
            )



    def add_session(self, session):
        #Добавляет новую завершенную сессию.

        sessions = self.load_sessions()


        # автоматическая нумерация

        session["id"] = len(sessions) + 1


        sessions.append(
            session
        )


        self.save_sessions(
            sessions
        )



    # Работа с настройками

    def load_settings(self):
        #Загружает настройки пользователя.

        try:

            with open(
                self.settings_file,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)



        except (
            json.JSONDecodeError,
            FileNotFoundError
        ):

            return {

                "work_time":
                    DEFAULT_WORK_TIME,

                "short_break":
                    DEFAULT_SHORT_BREAK,

                "long_break":
                    DEFAULT_LONG_BREAK,

                "long_break_interval":
                    LONG_BREAK_INTERVAL
            }



    def save_settings(self, settings):
        #Сохраняет настройки.

        with open(
            self.settings_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                settings,
                file,
                indent=4,
                ensure_ascii=False
            )



    def update_setting(
            self,
            key,
            value
    ):
        #Изменяет одну настройку.


        settings = self.load_settings()


        settings[key] = value


        self.save_settings(
            settings
        )

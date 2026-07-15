# ==================================================
# Создание хранилища
# ==================================================

def test_storage_creates_files(tmp_path):

    sessions_file = (
        tmp_path / "sessions.json"
    )

    settings_file = (
        tmp_path / "settings.json"
    )


    storage = Storage()


    storage.sessions_file = sessions_file

    storage.settings_file = settings_file


    storage._create_files()


    assert sessions_file.exists()

    assert settings_file.exists()



# ==================================================
# Сохранение и загрузка сессий
# ==================================================

def test_save_and_load_sessions(tmp_path):

    storage = Storage()


    storage.sessions_file = (
        tmp_path / "sessions.json"
    )


    sessions = [

        {
            "id": 1,
            "duration": 25,
            "completed": True
        }

    ]


    storage.save_sessions(
        sessions
    )


    result = storage.load_sessions()


    assert result == sessions



# ==================================================
# Добавление новой сессии
# ==================================================

def test_add_session(tmp_path):

    storage = Storage()


    storage.sessions_file = (
        tmp_path / "sessions.json"
    )


    storage.save_sessions([])


    session = {

        "duration": 25,

        "completed": True,

        "session_type": "work"

    }


    storage.add_session(
        session
    )


    result = storage.load_sessions()


    assert len(result) == 1

    assert result[0]["id"] == 1

    assert result[0]["duration"] == 25



# ==================================================
# Сохранение настроек
# ==================================================

def test_save_and_load_settings(tmp_path):

    storage = Storage()


    storage.settings_file = (
        tmp_path / "settings.json"
    )


    settings = {

        "work_time": 30,

        "short_break": 10,

        "long_break": 20

    }


    storage.save_settings(
        settings
    )


    result = storage.load_settings()


    assert result == settings



# ==================================================
# Изменение одной настройки
# ==================================================

def test_update_setting(tmp_path):

    storage = Storage()


    storage.settings_file = (
        tmp_path / "settings.json"
    )


    storage.save_settings({

        "work_time": 25,

        "short_break": 5

    })


    storage.update_setting(
        "work_time",
        40
    )


    result = storage.load_settings()


    assert result["work_time"] == 40

    assert result["short_break"] == 5



# ==================================================
# Загрузка отсутствующего файла
# ==================================================

def test_load_sessions_without_file(tmp_path):

    storage = Storage()


    storage.sessions_file = (
        tmp_path / "not_exists.json"
    )


    result = storage.load_sessions()


    assert result == []



# ==================================================
# Поврежденный JSON
# ==================================================

def test_load_broken_json(tmp_path):

    storage = Storage()


    file = (
        tmp_path / "sessions.json"
    )


    storage.sessions_file = file


    with open(
        file,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            "broken json"
        )


    result = storage.load_sessions()


    assert result == []



# ==================================================
# Проверка формата JSON
# ==================================================

def test_saved_file_is_valid_json(tmp_path):

    storage = Storage()


    storage.sessions_file = (
        tmp_path / "sessions.json"
    )


    data = [

        {
            "id": 1,
            "duration": 25
        }

    ]


    storage.save_sessions(
        data
    )


    with open(
        storage.sessions_file,
        "r",
        encoding="utf-8"
    ) as file:

        loaded = json.load(
            file
        )


    assert loaded == data

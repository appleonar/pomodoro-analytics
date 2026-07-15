# Pomodoro Timer with Analytics — учебная ознакомительная практика 2026

**Студентка:** Пшенко Алёна Александровна  
**Группа:** БИН-24-1  
**Вариант:** Б-11 — Таймер Pomodoro с аналитикой  
**Язык:** Python 3.12

---

# Описание

**Pomodoro Timer with Analytics** — настольное приложение, реализующее технику управления временем Pomodoro. Программа позволяет запускать рабочие и интервалы отдыха, автоматически переключаться между режимами, сохранять историю завершённых сессий и анализировать продуктивность пользователя.

Приложение разработано на языке **Python** с использованием библиотеки **Tkinter**. Данные пользователя хранятся в формате **JSON**, реализован экспорт статистики в CSV, а также предусмотрены автоматизированные тесты и возможность запуска проекта в контейнере Docker.

---

# Основные возможности

* запуск таймера Pomodoro;
* автоматическое переключение между рабочими сессиями и отдыхом;
* настройка продолжительности работы и отдыха;
* сохранение истории завершённых Pomodoro-сессий;
* просмотр статистики продуктивности;
* анализ активности пользователя;
* экспорт статистики в CSV;
* хранение пользовательских настроек;
* автоматическое создание файлов данных при первом запуске;
* модульное построение приложения.

---

# Структура репозитория

```text
.
├── app.py                      # точка входа приложения
├── config.py                   # основные настройки проекта
├── requirements.txt            # зависимости проекта
├── Dockerfile                  # контейнеризация приложения
├── README.md                   # документация проекта
│
├── core/
│   ├── timer.py                # логика таймера Pomodoro
│   ├── storage.py              # хранение данных
│   ├── analytics.py            # аналитика продуктивности
│   ├── statistics.py           # расчёт статистики
│   └── export.py               # экспорт данных
│
├── gui/
│   ├── window.py               # главное окно приложения
│   ├── widgets.py              # пользовательские элементы интерфейса
│   └── dialogs.py              # диалоговые окна
│
├── data/
│   ├── sessions.json           # журнал завершённых сессий
│   └── settings.json           # пользовательские настройки
│
├── exports/                    # экспортированные файлы
│
└── tests/
    ├── test_timer.py           # тестирование таймера
    ├── test_storage.py         # тестирование хранения данных
    ├── test_statistics.py      # тестирование статистики
    └── test_integration.py     # интеграционные тесты
```

---

# Требования

Для работы приложения необходимо:

* Python **3.12** или новее;
* установленный Tkinter;
* pip;
* pytest (для запуска тестов);
* Git (для клонирования репозитория);
* Docker (необязательно, только для контейнерного запуска).

---

# Установка и запуск

## Локальный запуск

## Linux

### 1. Клонировать репозиторий

```bash
git clone https://github.com/appleonar/pomodoro-analytics.git

cd pomodoro-analytics
```

### 2. Установить Python

```bash
sudo apt update

sudo apt install python3 python3-pip python3-venv python3-tk
```

### 3. Создать виртуальное окружение

```bash
python3 -m venv venv
```

### 4. Активировать окружение

```bash
source venv/bin/activate
```

### 5. Установить зависимости

```bash
pip install -r requirements.txt
```

### 6. Запустить программу

```bash
python3 app.py
```

---

## macOS

### 1. Клонировать репозиторий

```bash
git clone https://github.com/appleonar/pomodoro-analytics.git

cd pomodoro-analytics
```

### 2. Проверить наличие Python

```bash
python3 --version
```

При необходимости установить Python через официальный установщик или Homebrew.

### 3. Создать виртуальное окружение

```bash
python3 -m venv venv
```

### 4. Активировать окружение

```bash
source venv/bin/activate
```

### 5. Установить зависимости

```bash
pip install -r requirements.txt
```

### 6. Запустить приложение

```bash
python3 app.py
```

---

## Windows

### 1. Клонировать репозиторий

```powershell
git clone https://github.com/appleonar/pomodoro-analytics.git

cd pomodoro-analytics
```

### 2. Создать виртуальное окружение

```powershell
python -m venv venv
```

### 3. Активировать окружение

```powershell
venv\Scripts\activate
```

Если используется PowerShell и появляется сообщение о запрете выполнения сценариев:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

После этого снова выполните:

```powershell
venv\Scripts\activate
```

### 4. Установить зависимости

```powershell
pip install -r requirements.txt
```

### 5. Запустить приложение

```powershell
python app.py
```

---

# Запуск в Docker

Приложение **Pomodoro Timer with Analytics** использует графический интерфейс **Tkinter**.

Docker-контейнеры работают в изолированной среде и не имеют прямого доступа к рабочему столу пользователя. Поэтому для отображения окна приложения необходимо использовать внешний **X-сервер**.

Для разных операционных систем требуется различная настройка графического окружения.
.

---

# Linux

## 1. Клонирование репозитория

Открыть терминал и выполнить:

```bash
git clone https://github.com/appleonar/pomodoro-analytics.git

cd pomodoro-analytics
````

---

## 2. Разрешение доступа Docker к X-серверу

Linux использует встроенный X-сервер, поэтому необходимо разрешить контейнеру подключение к нему:

```bash
xhost +local:docker
```

---

## 3. Сборка Docker-образа

Из корневой директории проекта выполнить:

```bash
docker build -t pomodoro-analytics .
```

После успешной сборки появится Docker-образ:

```text
pomodoro-analytics
```

---

## 4. Запуск приложения

Запустить контейнер:

```bash
docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix pomodoro-analytics
```

После запуска должно открыться главное окно приложения.

---

## 6. Завершение работы

После окончания работы рекомендуется отключить доступ контейнера к X-серверу:

```bash
xhost -local:docker
```

---

# macOS

## 1. Клонирование репозитория

Открыть Terminal и выполнить:

```bash
git clone https://github.com/appleonar/pomodoro-analytics.git

cd pomodoro-analytics
```

---

## 2. Установка X-сервера

macOS не содержит встроенного X-сервера, поэтому необходимо установить **XQuartz**.

Установка через Homebrew:

```bash
brew install --cask xquartz
```

После установки необходимо перезагрузить компьютер.

---

## 3. Настройка XQuartz

Запустить приложение:

```text
Applications → Utilities → XQuartz
```

Открыть:

```text
XQuartz → Settings → Security
```

Включить параметр:

```text
Allow connections from network clients
```

После изменения настроек необходимо перезапустить XQuartz.

---

## 4. Настройка переменной DISPLAY

В терминале выполнить:

```bash
export DISPLAY=$(hostname):0
```

Разрешить внешние подключения:

```bash
xhost +
```

---

## 5. Сборка Docker-образа

Перейти в директорию проекта:

```bash
cd pomodoro-analytics
```

Выполнить:

```bash
docker build -t pomodoro-analytics .
```

---

## 6. Запуск приложения

Запустить контейнер:

```bash
docker run --rm -e DISPLAY=$DISPLAY pomodoro-analytics
```

Окно приложения появится через XQuartz.

---

## 7. Завершение работы

После завершения работы отключить доступ:

```bash
xhost -
```

---

# Windows

## 1. Клонирование репозитория

Открыть PowerShell и выполнить:

```powershell
git clone https://github.com/appleonar/pomodoro-analytics.git

cd pomodoro-analytics
```

---

## 2. Установка X-сервера

Windows не имеет встроенного X-сервера, поэтому необходимо установить дополнительное программное обеспечение.

Рекомендуется использовать:

```text
VcXsrv Windows X Server
```
Установить можно по ссылке:

```
https://sourceforge.net/projects/vcxsrv/
```

После установки запустить:

```text
XLaunch
```

Настройки запуска:

1. Выбрать:

```text
Multiple windows
```

2. Далее:

```text
Start no client
```

3. Включить:

```text
Disable access control
```

После запуска VcXsrv должен работать в фоновом режиме.

---

## 3. Определение IP-адреса компьютера

Открыть PowerShell:

```powershell
ipconfig
```

Найти IPv4-адрес активного подключения.

Пример:

```text
IPv4 Address . . . . . : 192.168.56.1
```

---

## 4. Настройка переменной DISPLAY

В PowerShell выполнить:

```powershell
$env:DISPLAY="192.168.56.1:0.0"
```

где `192.168.56.1` необходимо заменить на собственный IPv4-адрес.

---

## 5. Сборка Docker-образа

В корневой директории проекта выполнить:

```powershell
docker build -t pomodoro-analytics .
```

---

## 6. Запуск контейнера

Запустить приложение:

```powershell
docker run --rm -e DISPLAY=$env:DISPLAY pomodoro-analytics
```

После успешного запуска окно Tkinter появится через VcXsrv.

---

# Проверка работы контейнера

После запуска приложения должны быть доступны:

* главное окно Pomodoro-таймера;
* запуск рабочей сессии;
* переход в режим отдыха;
* кнопки паузы и сброса;
* настройка длительности интервалов;
* сохранение истории сессий;
* просмотр статистики;
* экспорт данных.

---

# Возможные ошибки

## Ошибка подключения к дисплею

```text
_tkinter.TclError: couldn't connect to display
```

Причины:

* X-сервер не запущен;
* неверно указана переменная `DISPLAY`;
* контейнеру запрещён доступ к X-серверу.

Решение:

* проверить запуск XQuartz/VcXsrv;
* проверить значение переменной `DISPLAY`;
* повторить настройку доступа X-сервера.

---

## Ошибка отсутствия Tkinter

```text
ModuleNotFoundError: No module named 'tkinter'
```

Причина:

В контейнере отсутствуют необходимые зависимости Python.

Решение:

Проверить содержимое `Dockerfile` и наличие установки Tkinter внутри образа.

---

# Остановка контейнера

Если приложение запущено в текущем терминале:

```text
Ctrl + C
```

Контейнер будет автоматически удалён благодаря параметру:

```bash
--rm
```




---

# Запуск тестов

Запуск всех тестов:

Перед запуском тестов убедитесь, что установлены все зависимости:

```bash
pip install -r requirements.txt
```

Запуск всех тестов
```bash
pytest tests
```

## Запуск отдельного тестового модуля

Тестирование таймера:

```bash
pytest tests/test_timer.py
```

Тестирование хранения данных:

```bash
pytest tests/test_storage.py
```

Тестирование статистики:

```bash
pytest tests/test_statistics.py
```

Интеграционное тестирование:

```bash
pytest tests/test_integration.py
```
## Подробный вывод результатов

Для отображения подробной информации о выполнении тестов рекомендуется использовать ключ -v:

```bash
pytest -v
```

или
```bash
pytest tests -v
```
---

# Используемые технологии

* Python 3.12
* Tkinter
* JSON
* pathlib
* datetime
* csv
* pytest
* Docker
* Git

---

# Хранение данных

После первого запуска автоматически создаётся директория `data` с файлами:

* `sessions.json` — хранит историю завершённых Pomodoro-сессий;
* `settings.json` — хранит пользовательские настройки приложения.

Экспортируемые файлы сохраняются в директорию `exports`.

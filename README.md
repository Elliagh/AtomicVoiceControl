# AtomicVoiceControl

### Как завести у себя (вводите по одной):

#### Если еще не клонировали с github
```shell
git clone https://github.com/Elliagh/AtomicVoiceControl.git
```

#### Установка виртуального окружения
```shell

(для Linux)

python3 -m venv venv
source ./venv/bin/activate

(для Windows)

python -m venv venv
venv\Scripts\activate.bat
```

#### Установка необходимых компонентов
```shell
pip install -r requirements.txt
```

## Не забываем и про конфигурацию `venv` в PyCharm если вы работаете там

Переходим в `File > Settings > Project: test > Python Interpreter`

Смотрим на `Python Interpreter` и там должен быть `venv` от test

Если его нет, то добавляем: `Add Interpreter` > `Add Local Interpreter` > `Environment: Existing`

Выбираем свой `venv`, файл `venv/bin/python`


### Для запуска используем:

```shell
uvicorn main:app

или запускаем main.py
```

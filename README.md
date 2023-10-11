# AtomicVoiceControl

### Как завести у себя (вводите по одной):

#### Если еще не клонировали с github
```shell
git clone https://github.com/Elliagh/AtomicVoiceControl.git
cd test 
```

#### Установка виртуального окружения
```shell
python3 -m venv venv
source ./venv/bin/activate
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
```
### Для подключения к бд:
```shell
в файлах alembic.ini и settings.py изменить значение sqlalchemy.url на  
alembic.ini -> sqlalchemy.url = postgresql://user:password@host:port/db_name
settings.py -> default = "postgresql+asyncpg://user:password@host:port/db_name"
```
### Для поднятия сервисов баз для локальной разработки нужно запустить команду:

```
make up
```

Для накатывания миграций, если файла alembic.ini ещё нет, нужно запустить в терминале команду:

```
alembic init migrations
```

После этого будет создана папка с миграциями и конфигурационный файл для алембика.

- В alembic.ini нужно задать адрес базы данных, в которую будем катать миграции.
- Дальше идём в папку с миграциями и открываем env.py, там вносим изменения в блок, где написано

```
from myapp import mymodel
```
- Дальше вводим: ```alembic revision --autogenerate -m "comment"``` - делается при любых изменениях моделей
- Будет создана миграция
- Дальше вводим: ```alembic upgrade heads```

Для того, чтобы во время тестов нормально генерировались миграции нужно:
- сначала попробовать запустить тесты обычным образом. с первого раза все должно упасть
- если после падения в папке tests создались алембиковские файлы, то нужно прописать туда данные по миграхам
- если они не создались, то зайти из консоли в папку test и вызвать вручную команды на миграции, чтобы файлы появились

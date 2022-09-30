# DevOps_Warehouse
Проект студентов МПУ по дисциплине "АПЖЦПО"

## Участники

| Учебная группа | Имя пользователя | ФИО                      |
|----------------|------------------|--------------------------|
| 201-351        | @TrttiTrttu      | Летов Г. В.              |
| 201-351        | @Alex9781        | Змеёв А. Ю.              |

## Стек
Python 3 + Flask

## Сборка
Создать файл app/.env:
```
FLASK_APP=app.py
FLASK_DEBUG=true

DB_USER=user
DB_PASSWORD=password
DATABASE=database_name
DB_ROOT_PASSWORD=password
```
Запустить docker-compose файл
```
docker-compose --env-file ./app/.env up
```

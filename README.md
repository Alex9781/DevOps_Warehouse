# DevOps_Warehouse
Проект студентов МПУ по дисциплине "АПЖЦПО"

## Участники

| Учебная группа | Имя пользователя | ФИО                      |
|----------------|------------------|--------------------------|
| 201-351        | @TrttiTrttu      | Летов Г. В.              |
| 201-351        | @Alex9781        | Змиёв А. Ю.              |

## Стек
Python 3 + Flask

## Сборка
Создать файл app/.env:
```
FLASK_APP=app.py
FLASK_DEBUG=true

SECRET_KEY=some-secret-key

MYSQL_USER=user
MYSQL_PASSWORD=user_password
MYSQL_DATABASE=warehouse
MYSQL_ROOT_PASSWORD=root_password
```
Создать docker-compose.yaml
```
version: "3"
services:
  database:
    container_name: database
    hostname: database
    image: mysql
    volumes:
      - ./db:/var/lib/mysql
    env_file:
      - ./app/.env
    ports:
      - 3306:3306
    restart: unless-stopped
  flask:
    container_name: flask
    hostname: flask
    image: url
    env_file:
      - ./app/.env
    ports:
      - "9000:9000"
    depends_on:
      - database
    restart: always

```
Запустить docker-compose файл
```
docker-compose up
```

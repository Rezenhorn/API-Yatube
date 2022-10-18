# Описание:
- Проект **api_final_yatube** представляет собой API для сервиса микроблогов Yatube.
- С помощью API доступны операции с моделями Post, Group, Comment, Follow, User.
- Полный список операций доступен по [ссылке](http://127.0.0.1:8000/redoc/) (работает на запущенном сервере).
- В проекте реализована аутентификация по JWT-токену.
# Примеры запросов:
- GET /api/v1/posts/ - получить список всех постов
- POST /api/v1/posts/ - опубликовать пост
- GET /api/v1/follow/ - получить все подписки пользователя, сделавшего запрос
- DELETE /api/v1/posts/{post_id}/comments/{id}/ - удаление комментария к посту
- PATCH /api/v1/posts/{post_id}/comments/{id}/ - частичное обновление комментария к публикации по id
# Как запустить проект:

## Клонировать репозиторий и перейти в него:
```
git clone https://github.com/Rezenhorn/api_final_yatube.git
```
## Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
## Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
## Выполнить миграции:
```
python3 manage.py migrate
```
## Запустить проект:
```
python3 manage.py runserver
```

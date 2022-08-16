# Проект «API для Yatube»

### Краткое описание проекта

Учебный проект API для социальной сети. Пользователи могут публиковать посты,
просматривать чужие посты, подписываться на авторов и комментировать их записи.
Для аутентификации используются JWT-токены. Аутентифицированным пользователям
разрешено изменение и удаление своего контента; в остальных случаях доступ
предоставляется только для чтения.

### **Стек**

![python version](https://img.shields.io/badge/Python-3.7-green)
![django version](https://img.shields.io/badge/Django-2.2-green)
![djangorestframework version](https://img.shields.io/badge/DRF-3.12-green)
![simplejwt version](https://img.shields.io/badge/DRFsimplejwt-4.7-green)

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/drode1/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
. venv/bin/activate
```

```
python -m pip install --upgrade pip
```    

Установить зависимости из файла requirements.txt:

``` 
pip install -r requirements.txt
```   

Выполнить миграции:

```
python manage.py migrate
```       

Запустить проект:

```
python manage.py runserver
```

### Документация к API доступна по адресу

**api/v1/redoc/**


### Примеры использования

Придумайте новую пару «логин-пароль» и отправьте POST-запрос на .../api/v1/users/, передав их в полях username и password.

Теперь можно получить токен: отправьте POST-запрос на эндпоинт .../api/v1/jwt/create/, передав действующий логин и пароль в полях username и password. 

API вернёт JWT-токен:

```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMDk0MTQ3NywianRpIjoiODUzYzE5MTg5NzMwNDQwNTk1ZjI3ZTBmOTAzZDcxZDEiLCJ1c2VyX2lkIjoxfQ.0vJBPIUZG4MjeU_Q-mhr5Gqjx7sFlO6AShlfeINK8nA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIwODU1Mzc3LCJqdGkiOiJkY2EwNmRiYTEzNWQ0ZjNiODdiZmQ3YzU2Y2ZjNGE0YiIsInVzZXJfaWQiOjF9.eZfkpeNVfKLzBY7U0h5gMdTwUnGP3LjRn5g8EIvWlVg"
} 
```
Токен вернётся в поле access, а данные из поля refresh пригодятся для обновления токена. Этот токен также надо будет передавать в заголовке каждого запроса, в поле Authorization. Перед самим токеном должно стоять ключевое слово Bearer и пробел.

Пример POST-запроса. Регистрация нового пользователя

```
POST /api/v1/auth/signup/

Request samples

{
  "email": "string",
  "username": "string"
}
```

Пример POST-запроса. Добавление нового произведения

```
POST /api/v1/titles/

Request samples

{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```

Пример GET-запроса. Получить информацию о произведении.
```
GET /api/v1/titles/{title_id}/
```

Пример POST-запроса. Создать категорию.

```
POST /api/v1/titles/

Request samples

{
  "name": "string",
  "slug": "string"
}
```

Пример GET-запроса. Получить список всех категорий.
```
GET /api/v1/categories/
```

Пример POST-запроса. Добавить новый отзыв.

```
POST /api/v1/titles/{title_id}/reviews/

Request samples

{
  "text": "string",
  "score": 1
}
```

Пример GET-запроса. Получить список всех отзывов.
```
GET /api/v1/titles/{title_id}/reviews/
```
Пример POST-запроса. Добавить новый комментарий для отзыва.

```
POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/

Request samples

{
  "text": "string"
}
```
Пример GET-запроса. Получить комментарий для отзыва по id.
```
GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```


### Импорт тестовых данных

Для проверки работы проекта можно наполнить проект тестовыми данными, для этого
можно ввести команду

```
python manage.py import
```

Данная команда импортирует данные по:

- категориям;
- комментариям;
- жанрам;
- отзывам;
- произведениям;
- пользователям.

___

## Команда

- [Антон Росляков](https://github.com/Antonros)
- [Егор Ремезов](https://github.com/drode1)
- [Павел Зияев](https://github.com/p0lzi)
- [Яндекс Практикум](https://github.com/yandex-praktikum/)

___ 

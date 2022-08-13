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

### Примеры использования
from csv import DictReader

from django.core.management import BaseCommand

# Импорт моделей
from reviews.models import Category, Genre, User, Review, Comment, Title


class Command(BaseCommand):
    help = "Загрузка данных в БД из csv"

    # Список переменных для импорта данных в модели
    models = {
        'users_category_genre':
            (
                (User, 'users'),
                (Category, 'category'),
                (Genre, 'genre'),
            ),
        'title':
            (
                (Title, 'titles'),
            ),
        'review_comment':
            (
                (Review, 'review'),
                (Comment, 'comments'),
            )
    }

    def users_category_genre(self):
        """ Метод импортирует пользователей, категории и жанры в БД. """
        for model, file in self.models.get('users_category_genre'):
            with open(f'static/data/{file}.csv', encoding='utf-8') as f:
                for row in DictReader(f):
                    if not model.objects.filter(**row).exists():
                        model.objects.create(**row)

    def titles(self):
        """ Метод импортирует произведения в БД. """

        for model, file in self.models.get('title'):
            with open(f'static/data/{file}.csv', encoding='utf-8') as f:
                for row in DictReader(f):
                    if not model.objects.filter(**row).exists():
                        category = Category.objects.get(pk=row['category'])
                        row.pop('category')
                        Title.objects.create(
                            **row,
                            category=category
                        )

    def reviews_comments_titles(self):
        """ Метод импортирует отзывы и комментарии произведения в БД. """

        for model, file in self.models.get('review_comment'):
            with open(f'static/data/{file}.csv', encoding='utf-8') as f:
                for row in DictReader(f):
                    if not model.objects.filter(**row).exists():
                        author = User.objects.get(pk=row['author'])
                        row.pop('author')
                        model.objects.create(
                            **row,
                            author=author
                        )

    def handle(self, *args, **options):
        """ Агрегирующий метод, который вызывается с помощью команды import
        и добавляет тестовые данные в БД. """

        self.users_category_genre()
        self.titles()
        self.reviews_comments_titles()

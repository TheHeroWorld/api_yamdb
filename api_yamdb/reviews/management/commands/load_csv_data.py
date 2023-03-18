from csv import DictReader
from os.path import exists

from django.contrib.staticfiles.finders import find
from django.core.management import BaseCommand, CommandError

from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User

MODELS_FILES = {
    'users': User,
    'category': Category,
    'titles': Title,
    'review': Review,
    'comments': Comment,
    'genre': Genre,
}


def create_table(model, row):
    if model == User:
        User.objects.create(
            id=row['id'],
            username=row['username'],
            email=row['email'],
            role=row['role'],
            bio=row['bio'],
            first_name=row['first_name'],
            last_name=row['last_name']
        )
    elif model == Category:
        Category.objects.create(
            id=row['id'],
            name=row['name'],
            slug=row['slug'],
        )
    elif model == Genre:
        Genre.objects.create(
            id=row['id'],
            name=row['name'],
            slug=row['slug'],
        )
    elif model == Title:
        Title.objects.create(
            id=row['id'],
            name=row['name'],
            year=row['year'],
            category=Category.objects.get(
                id=row['category']
            ),
        )
    elif model == Review:
        Review.objects.create(
            id=row['id'],
            title=Title.objects.get(id=row['title_id']),
            text=row['text'],
            author=User.objects.get(id=row['author']),
            score=row['score'],
            pub_date=row['pub_date'],
        )
    elif model == Comment:
        Comment.objects.create(
            id=row['id'],
            review=Review.objects.get(id=row['review_id']),
            text=row['text'],
            author=User.objects.get(id=row['author']),
            pub_date=row['pub_date'],
        )


class Command(BaseCommand):
    """Класс загрузки базы данных."""

    def handle(self, *args, **options):
        for filename, model in MODELS_FILES.items():
            csv_file = find(f'data/{filename}.csv')
            if exists(csv_file):
                try:
                    for row in DictReader(open(csv_file, encoding='utf-8')):
                        create_table(model, row)
                except ValueError as error:
                    raise CommandError(f'Ошибка добавления объекта: {error}')
            else:
                print(f'Загрузка {filename}.csv невозможна, не найден файл.')

            print(f'{model.__name__}: успешная загрузка данных.')

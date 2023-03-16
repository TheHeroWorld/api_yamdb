from csv import DictReader

from django.core.management.base import BaseCommand

from reviews.models import (Category, Genre, Title)


class Command(BaseCommand):
    help = 'Загрузка данных из csv файлов'

    def handle(self, *args, **options):
        for row in DictReader(open('static/data/category.csv')):
            category = Category(id=row['id'], name=row['name'],
                                slug=row['slug']
                                )
            category.save()

        for row in DictReader(open('static/data/genre/.csv')):
            genre = Genre(id=row['id'], name=row['name'], slug=row['slug'])
            genre.save()

        for row in DictReader(open('static/data/titles/.csv')):
            titles = Title(id=row['id'], name=row['name'],
                           year=row['year'], category=row['category']
                           )
            titles.save()

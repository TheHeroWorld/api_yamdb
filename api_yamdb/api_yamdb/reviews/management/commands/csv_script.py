from csv import DictReader

from django.core.management.base import BaseCommand

from reviews.models import (Category, Comments, Genre, Genre_Title, Review,
                            Title, Users)

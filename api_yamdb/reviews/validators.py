from django.core.exceptions import ValidationError
from django.utils import timezone


def year_validator(value):
    min_year = 0
    max_year = timezone.now().year
    if not (min_year <= value <= max_year):
        raise ValidationError('Неверный год создания')

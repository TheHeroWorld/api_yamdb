from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .validators import year_validator


User = get_user_model()


class BaseDate(models.Model):
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации отзыва',
        help_text='Дата заполняется автоматически при сохрании'
    )

    class Meta:
        abstract = True


class Category(models.Model):

    name = models.CharField(
        verbose_name='Категория',
        max_length=256,
        db_index=True
    )
    slug = models.SlugField(
        verbose_name='Cлаг',
        unique=True,
        max_length=settings.DEFAULT_FIELD_SIZE
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Жанр',
        max_length=256,
        db_index=True
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        unique=True,
        max_length=settings.DEFAULT_FIELD_SIZE
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):

    name = models.CharField(
        verbose_name='Произведение',
        max_length=256,
        db_index=True
    )
    year = models.PositiveSmallIntegerField(
        validators=[year_validator],
        verbose_name='Год создания произведения'
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        related_name='titles',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_index=True
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=300,
        blank=True,
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        related_name='titles',
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class Review(BaseDate):

    text = models.TextField(verbose_name='Текст отзыва')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    score = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(
                1, message='Значение может быть от 1 до 10'
            ),
            MaxValueValidator(
                10, message='Значение может быть от 1 до 10'
            )
        ],
        verbose_name='Рейтинг',
        help_text='Укажите рейтинг отзыва от 1 до 10'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Название произведения'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-pub_date']
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique review')
        ]

    def __str__(self):
        return self.text[:settings.DEFAULT_FIELD_SIZE]


class Comment(BaseDate):

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )
    text = models.TextField(
        verbose_name='Комментарий',
        help_text='Напишите Ваш комментарий к отзыву'
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-pub_date']

    def __str__(self):
        return self.text[:settings.DEFAULT_FIELD_SIZE]

from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    validate_slug)
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Review(models.Model):
    """Создан класс отзывов"""
    text = models.TextField(
        verbose_name='text'
        )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add = True,
        db_index=True
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='произведение',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name='unique_review_title',
                fields=('author', 'title')
            )
        ]
        ordering = ('pub_date', 'id')


    score = models.PositiveIntegerField(
        verbose_name='оценка',
        validators=[
            MinValueValidator(
                1, message='Оценка ниже допустимой'
            ),
            MaxValueValidator(
                10, message='Оценка выше допустимой'
            ),
        ]
    )


class Comment(models.Model):
    """Создан класс комментариев"""
    text=models.TextField(
        verbose_name='text'
    ),
    author=models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    ),
    pub_date=models.DateField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        db_index=True
    ),
    reviews=models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name='unique_comment_title',
                fields=('author','reviews')
            )
        ]
        ordering=['pub_date','id']

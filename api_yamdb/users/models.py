from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import RegexValidator


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    ROLES = (
        (ADMIN, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (USER, 'Пользователь')
    )
    bio = models.TextField(
        verbose_name='Биография',
        blank=True
    )
    email = models.EmailField(
        verbose_name='E-mail',
        null=False,
        blank=False,
        max_length=254,
        unique=True
    )
    role = models.CharField(
        max_length=settings.DEFAULT_FIELD_SIZE,
        choices=ROLES,
        default=USER,
    )
    username = models.CharField(
            verbose_name='Имя пользователя',
            max_length=150,
            unique=True,
            validators=[
                RegexValidator(
                    regex='^[a-zA-Z0-9_]*$',
                    message='Имя пользователя может содержать только буквы, цифры и символ подчеркивания'
                )
            ]
        )
    
    def validate_username(value): 
        if value.lower() == 'me': 
            raise ValidationError( 
                f'{value} зарезервированно системой.' 
            ) 
        if not re.match(r'^[\w.@+-]+', value): 
            raise ValidationError( 
                f'{value} содержит неизвестные символы.')

    def __str__(self):
        return f'{self.username} ({self.email})'


    class Meta:
        ordering = ('-id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='username_email'
            ),
        ]

    def clean(self):
        if self.username == 'me':
            raise ValidationError('Me недоступно для регистрации')
        super().clean()

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

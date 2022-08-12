from django.contrib.auth.models import AbstractUser
from django.db import models

USER_ROLES_CHOICES = (
    ('user', 'user'),
    ('moderator', 'moderator'),
    ('admin', 'admin')
)


class User(AbstractUser):
    """ Модель пользователя. """

    role = models.CharField('Роль пользователя', choices=USER_ROLES_CHOICES,
                            max_length=250, default='user')
    bio = models.TextField('Биография', null=True, blank=True)

    confirmation_code = models.CharField('Код подтверждения', max_length=5,
                                         blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return self.username

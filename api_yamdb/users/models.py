from django.contrib.auth.models import AbstractUser
from django.db import models

USER_ROLES_CHOICES = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Администратор')
)


class User(AbstractUser):
    """ Модель пользователя. """

    role = models.CharField('Роль пользователя', choices=USER_ROLES_CHOICES,
                            max_length=250, default='user')
    bio = models.TextField('Биография', null=True, blank=True)

    confirmation_code = models.PositiveIntegerField('Код подтверждения',
                                                    blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return self.username

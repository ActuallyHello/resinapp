from django.db import models
from django.utils import timezone

from apps.resinauth.models.role import Role


class User(models.Model):
    login = models.CharField(max_length=50, unique=True, verbose_name='Логин')
    password_hash = models.CharField(max_length=255, verbose_name='Хэш пароля')
    salt = models.CharField(max_length=100, verbose_name='Соль')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    # Связь многие-ко-многим с ролями
    roles = models.ManyToManyField(
        Role,
        through='UserRole',
        through_fields=('user', 'role'),
        verbose_name='Роли пользователя'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'users'

    def __str__(self):
        return self.login
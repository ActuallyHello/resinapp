import hashlib
import secrets

from django.db import models
from django.utils import timezone

from apps.resinauth.models.role import Role
from apps.resincore.models.guide_item import GuideItem


class User(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=50, unique=True, verbose_name='Логин')
    password_hash = models.CharField(max_length=255, verbose_name='Хэш пароля')
    salt = models.CharField(max_length=100, verbose_name='Соль')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    state = models.ForeignKey(GuideItem, on_delete=models.DO_NOTHING, verbose_name='Состояние')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'users'

    def __str__(self):
        return self.login

    def __dict__(self):
        return {
            'id': self.id,
            'login': self.login,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }

    def set_password(self, raw_password: str):
        self.salt = secrets.token_hex(16)
        salted_password = self.salt + raw_password
        self.password_hash = hashlib.sha512(salted_password.encode()).hexdigest()
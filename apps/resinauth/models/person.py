from django.db import models
from django.utils import timezone

from apps.resinauth.models.user import User


class Person(models.Model):
    firstname = models.CharField(max_length=50, verbose_name='Имя')
    lastname = models.CharField(max_length=50, verbose_name='Фамилия')
    middlename = models.CharField(max_length=50, blank=True, null=True, verbose_name='Отчество')
    phone = models.CharField(max_length=20, unique=True, verbose_name='Телефон')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    # Связь один-к-одному с пользователем
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='person',
        verbose_name='Пользователь'
    )

    class Meta:
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'
        db_table = 'persons'

    def __str__(self):
        return f"{self.lastname} {self.firstname}"

    def get_full_name(self):
        """Возвращает полное имя"""
        parts = [self.lastname, self.firstname]
        if self.middlename:
            parts.append(self.middlename)
        return ' '.join(parts)
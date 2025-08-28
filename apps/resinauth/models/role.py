from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название роли')
    code = models.CharField(max_length=20, unique=True, verbose_name='Код роли')

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
        db_table = 'roles'  # Сохраняем имя таблицы как было

    def __str__(self):
        return f"{self.name} ({self.code})"
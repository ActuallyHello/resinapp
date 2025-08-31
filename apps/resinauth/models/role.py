from django.db import models


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Название роли')
    code = models.CharField(max_length=20, unique=True, verbose_name='Код роли')

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
        db_table = 'roles'  # Сохраняем имя таблицы как было

    def __str__(self):
        return f"{self.name} ({self.code})"

    def __dict__(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
        }
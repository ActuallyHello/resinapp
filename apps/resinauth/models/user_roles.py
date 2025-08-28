from django.db import models

from apps.resinauth.models.role import Role
from apps.resinauth.models.user import User


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name='Роль')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата назначения')

    class Meta:
        verbose_name = 'Роль пользователя'
        verbose_name_plural = 'Роли пользователей'
        db_table = 'user_roles'
        unique_together = [['user', 'role']]  # Уникальная пара

    def __str__(self):
        return f"{self.user.login} - {self.role.name}"
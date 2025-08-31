from django.db import migrations


def create_initial_roles(apps, schema_editor):
    Role = apps.get_model('resinauth', 'Role')

    # Создаем стандартные роли
    roles_data = [
        {
            'name': 'Администратор',
            'code': 'admin',
            'verbose_name': 'Администратор'
        },
        {
            'name': 'Пользователь',
            'code': 'user',
            'verbose_name': 'Пользователь'
        },
        {
            'name': 'Гость',
            'code': 'guest',
            'verbose_name': 'Гость'
        },
    ]

    for role_data in roles_data:
        Role.objects.get_or_create(
            code=role_data['code'],
            defaults={
                'name': role_data['name']
            }
        )


def reverse_initial_roles(apps, schema_editor):
    Role = apps.get_model('resinauth', 'Role')

    # Удаляем только те роли, которые мы создали
    initial_codes = ['admin', 'user', 'guest']
    Role.objects.filter(code__in=initial_codes).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('resinauth', '0001_initial'),  # Убедитесь, что это правильное имя предыдущей миграции
    ]

    operations = [
        migrations.RunPython(create_initial_roles, reverse_initial_roles),
    ]
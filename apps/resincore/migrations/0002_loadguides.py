from django.db import migrations


def create_initial_data(apps, schema_editor):
    Guide = apps.get_model('resincore', 'Guide')
    GuideItem = apps.get_model('resincore', 'GuideItem')

    # Создаем справочник "Состояние"
    status_guide, created = Guide.objects.get_or_create(
        code='status',
        defaults={'label': 'Состояние'}
    )

    # Создаем элементы справочника
    GuideItem.objects.get_or_create(
        guide=status_guide,
        code='created',
        defaults={'label': 'Создан'}
    )

    GuideItem.objects.get_or_create(
        guide=status_guide,
        code='deleted',
        defaults={'label': 'Удален'}
    )


def reverse_initial_data(apps, schema_editor):
    Guide = apps.get_model('resincore', 'Guide')
    GuideItem = apps.get_model('resincore', 'GuideItem')

    # Удаляем созданные данные (для отката миграции)
    GuideItem.objects.filter(guide__code='status').delete()
    Guide.objects.filter(code='status').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('resincore', '0001_initial'),  # предыдущая миграция
    ]

    operations = [
        migrations.RunPython(create_initial_data, reverse_initial_data),
    ]
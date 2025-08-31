from django.db import models

from apps.resincore.models.guide import Guide


class GuideItem(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)

    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, verbose_name='Справочник', related_name='guide_items')

    class Meta:
        verbose_name = 'Элемент справочника'
        db_table = 'guide_item'

    def natural_key(self):
        return (self.code,)

    def __str__(self):
        return f"{self.label} - {self.code}"

    def to_dict(self):
        return {
            'id': self.id,
            'label': self.label,
            'code': self.code,
            'guide': self.guide_id,
        }

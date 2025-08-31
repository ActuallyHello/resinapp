from django.db import models


class Guide(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Справочник'
        db_table = 'guide'

    def natural_key(self):
        return (self.code,)

    def __str__(self):
        return f"{self.label} - {self.code}"

    def to_dict(self):
        return {
            'id': self.id,
            'label': self.label,
            'code': self.code,
        }

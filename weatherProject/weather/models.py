from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    temperature = models.PositiveIntegerField(null=True)
    conditions = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.

class EUModel(models.Model):
    to = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    y = models.IntegerField()
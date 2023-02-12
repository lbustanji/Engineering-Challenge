from django.db import models
from django.utils import timezone

class Trade(models.Model):

    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    side = models.CharField(max_length=4)
    strategy = models.CharField(max_length=20)

class PnlData(models.Model):
    strategy = models.CharField(max_length=10)
    value = models.FloatField(default=0)
    unit = models.CharField(max_length=10)
    capture_time = models.DateTimeField(default=timezone.now)
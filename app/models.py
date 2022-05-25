from django.db import models


class GoogleSheets(models.Model):
    id = models.IntegerField(primary_key=True)
    order = models.IntegerField()
    price_dollar = models.FloatField()
    price_ruble = models.FloatField()
    delivery_time = models.DateField()

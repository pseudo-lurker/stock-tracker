from django.db import models


class Company(models.Model):
    ticker = models.CharField(max_length=4)
    name = models.CharField(max_length=10)
    last_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)


class PriceChangeEvent(models.Model):
    company = models.ForeignKey(to='Company', on_delete=models.PROTECT)
    before_price = models.DecimalField(max_digits=7, decimal_places=2)
    after_price = models.DecimalField(max_digits=7, decimal_places=2)
    flat_change = models.DecimalField(max_digits=7, decimal_places=2)
    percentage_change = models.DecimalField(max_digits=4, decimal_places=2)
    changed = models.DateTimeField()

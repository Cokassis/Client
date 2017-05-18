from django.db import models

# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=30)
    material = models.ManyToManyField(
        'food.Material',
        through='MatSellInfo',
        through_fields=('supplier', 'material')
    )


class MatSellInfo(models.Model):
    unit_price = models.FloatField()
    in_stock = models.BooleanField()
    producing_area = models.CharField(max_length=30, null=True)
    unit = models.CharField(max_length=30)
    supplier = models.ForeignKey(Supplier)
    material = models.ForeignKey('food.Material')
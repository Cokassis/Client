from django.db import models
from food.models import Material

# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=30)
    material = models.ManyToManyField(
        Material,
        through='MatSellInfo',
        through_fields=('supplier', 'material')
    )


class MatSellInfo(models.Model):
    unitPrice = models.FloatField()
    inStock = models.BooleanField()
    supplier = models.ForeignKey(Supplier)
    material = models.ForeignKey(Material)
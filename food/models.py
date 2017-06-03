from django.db import models

# Create your models here.


class Dish(models.Model):
    name = models.CharField(max_length=30)
    like = models.IntegerField(default=5)

    def estimate_price(self):
        from supplier.models import Supplier, MatSellInfo
        materials = self.material_set.all()
        price = 0
        for a_material in materials:
            a_dish_mat = DishMat.objects.get(
                dish__id=self.id,
                material_id=a_mateiral.id
            )
            quantity = a_dish_mat.quantity
            mean_weight = a_dish_mat.weight_range.mean_weight()
            amount = mean_weight * quantity
            unit_price = MatSellInfo.objects.get(
                material__id=a_material.id,
                supplier__id=a_dish_mat.supplier.id
            ).unit_price
            price += unit_price * amount
        return price

    def calculate_discount(self):
        return 1.0


class DishMat(models.Model):
    quantity = models.IntegerField()
    unit = models.CharField(max_length=30)
    dish = models.ForeignKey('Dish')
    material = models.ForeignKey('Material')
    weight_range = models.OneToOneField('WeightRange')
    supplier = models.OneToOneField('supplier.Supplier')


class DishPhoto(models.Model):
    photo = models.ImageField(upload_to='~/cokassis/image')
    dish = models.ForeignKey('Dish')


class Material(models.Model):
    abstract = models.CharField(max_length=30, null=True)
    alias = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, null=True)
    dish = models.ManyToManyField(
        'Dish',
        through='DishMat',
        through_fields=('material', 'dish'),
    )


class MaterialPhoto(models.Model):
    photo = models.ImageField(upload_to='~cokassis/image')
    material = models.ForeignKey('Material')


class WeightRange(models.Model):
    max_weight = models.FloatField()
    min_weight = models.FloatField()
    range_desc = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)
    material = models.ForeignKey('Material')

    def mean_weight(self):
        result = (self.max_weight + self.min_weight)/2
        return result

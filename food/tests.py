from django.test import TestCase
from food.models import Dish, Material

# Create your tests here.


class DishMaterialTestCase(TestCase):
    def setUp(self):
        Dish.objects.create(estPrice = 6.5, name = "番茄炒蛋", discount = 1.5, like = 5)
        Dish.objects.create(estPrice = 6.5, name = "番茄土豆片", discount = 1.5, like = 5)
        Material.objects.create({name: "番茄",
                                 breed: "大红番茄"})
        Material.objects.create({name: "番茄",
                                 breed: "粉红番茄"})
        Material.objects.create({name: "西红柿",
                                 breed: ""})

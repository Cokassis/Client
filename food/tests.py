from django.test import TestCase, Client
from food.models import Dish, Material

# Create your tests here.


class DishMaterialTestCase(TestCase):
    def setUp(self):
        Dish.objects.create(estPrice= 6.5,
                             name= "番茄炒蛋",
                             discount= 1.5,
                             like= 5)
        Dish.objects.create(estPrice= 9,
                             name= "番茄土豆片",
                             discount= 2.5,
                             like= 3)
        Dish.objects.create(estPrice= 19,
                             name= "红烧牛肉",
                             discount= 2.5,
                             like= 3)
        Dish.objects.create(estPrice= 19,
                             name= "酸辣土豆丝",
                             discount= 2.5,
                             like= 3)
        Dish.objects.create(estPrice= 19,
                             name= "糖醋排骨",
                             discount= 2.5,
                             like= 3)
        Material.objects.create(name= "番茄",
                                 breed= "大红番茄")
        Material.objects.create(name= "番茄",
                                 breed= "粉红番茄")
    def test_search_fanqie_return_corsp_dish_material(self):
        c = Client()
        resp = c.post('/search/', {'searchStr': '番茄'})
        resp_json = resp.json()
        dishes = resp_json['dishes']
        self.assertEqual(dishes[0]['name'], '番茄炒蛋')

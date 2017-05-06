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
        Dish.objects.create(estPrice= 9,
                             name= "(外婆真传)番茄打卤面",
                             discount= 2.5,
                             like= 3)
        Dish.objects.create(estPrice= 19,
                             name= "红烧牛肉",
                             discount= 2.5,
                             like= 3)
        Dish.objects.create(estPrice= 8,
                             name= "酸辣土豆丝",
                             discount= 1.5,
                             like= 4)
        Dish.objects.create(estPrice= 17,
                             name= "糖醋排骨",
                             discount= 2.5,
                             like= 5)
        Material.objects.create(name= "番茄",
                                 breed= "大红番茄")
        Material.objects.create(name= "番茄",
                                 breed= "粉红番茄")
        Material.objects.create(name= "番红茄",
                                 breed= "粉红番红茄")
    def test_search_fanqie_return_corsp_dish_material(self):
        c = Client()
        resp = c.get('/search/', {'search_str': '番茄'})
        resp_json = resp.json()
        dishes = resp_json['dishes']
        self.assertEqual(len(dishes), 3)
        self.assertEqual(dishes[0]['name'], '番茄炒蛋')
        self.assertEqual(dishes[0]['estPrice'], 6.5)
        self.assertEqual(dishes[0]['discount'], 1.5)
        self.assertEqual(dishes[0]['like'], 5)
        self.assertEqual(dishes[1]['name'], '番茄土豆片')
        self.assertEqual(dishes[1]['estPrice'], 9)
        self.assertEqual(dishes[1]['discount'], 2.5)
        self.assertEqual(dishes[1]['like'], 3)
        self.assertEqual(dishes[2]['name'], '(外婆真传)番茄打卤面')
        self.assertEqual(dishes[2]['estPrice'], 9)
        self.assertEqual(dishes[2]['discount'], 2.5)
        self.assertEqual(dishes[2]['like'], 3)
        materials = resp_json['materials']
        self.assertEqual(len(materials), 2)
        self.assertEqual(materials[0]['name'], '番茄')
        self.assertEqual(materials[0]['breed'], '大红番茄')
        self.assertEqual(materials[1]['name'], '番茄')
        self.assertEqual(materials[1]['breed'], '粉红番茄')


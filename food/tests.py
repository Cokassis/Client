from django.test import TestCase, Client
from food.models import Dish, Material, DishMat, WeightInterval
from supplier.models import Supplier, MatSellInfo

# Create your tests here.


class DishMaterialTestCase(TestCase):
    def setUp(self):
        fanQieChaoDan = Dish.objects.create(estPrice= 6.5,
                             name= "番茄炒蛋",
                             discount= 1.5,
                             like= 5)
        fanQieTuDouPian = Dish.objects.create(estPrice= 9,
                             name= "番茄土豆片",
                             discount= 2.5,
                             like= 3)
        fanQieDaLuMian = Dish.objects.create(estPrice= 9,
                             name= "(外婆真传)番茄打卤面",
                             discount= 2.5,
                             like= 3)
        hongShaoNiuRou = Dish.objects.create(estPrice= 19,
                             name= "红烧牛肉",
                             discount= 2.5,
                             like= 3)
        suanLaTuDouSi = Dish.objects.create(estPrice= 8,
                             name= "酸辣土豆丝",
                             discount= 1.5,
                             like= 4)
        tangCuPaiGu = Dish.objects.create(estPrice= 17,
                             name= "糖醋排骨",
                             discount= 2.5,
                             like= 5)
        daHongFanQie = Material.objects.create(name= "番茄",
                                 breed= "大红番茄")
        fenHongFanQie = Material.objects.create(name= "番茄",
                                 breed= "粉红番茄")
        fanHongQie = Material.objects.create(name= "番红茄",
                                 breed= "粉红番红茄")
        jidan = Material.objects.create(
            name="鸡蛋",
            breed="农家蛋"
        )
        pin_tai = Supplier.objects.create(
            name="品泰贸易有限公司"
        )
        lian_gui = Supplier.objects.create(
            name="连贵-蔬菜档"
        )
        MatSellInfo.objects.create(
            unitPrice=8,
            inStock=True,
            supplier=lian_gui,
            material=jidan
        )
        MatSellInfo.objects.create(
            unitPrice=3,
            inStock=True,
            supplier=pin_tai,
            material=daHongFanQie
        )
        daHongFanQieWeiInt0 = WeightInterval.obejcts.create(
            intervalMaxWeight=0.15,
            intervalMinWeight=0.1,
            material=daHongFanQie,
            intervalNote="小",
            unit="kg"
        )
        daHongFanQieWeiInt1 = WeightInterval.obejcts.create(
            intervalMaxWeight=0.2,
            intervalMinWeight=0.15,
            material=daHongFanQie,
            intervalNote="中",
            unit="kg"
        )
        daHongFanQieWeiInt2 = WeightInterval.obejcts.create(
            intervalMaxWeight=0.25,
            intervalMinWeight=0.2,
            material=daHongFanQie,
            intervalNote="大",
            unit="kg"
        )
        jiDanWeiInt = WeightInterval.obejcts.create(
            intervalMaxWeight=0.1,
            intervalMinWeight=0.05,
            material=jidan,
            intervalNote="",
            unit="kg"
        )
        DishMat.objects.create(
            dish=fanQieChaoDan,
            material=daHongFanQie,
            quantity=2,
            weightinterval=daHongFanQieWeiInt1
        )
        DishMat.objects.create(
            dish=fanQieChaoDan,
            material=jidan,
            quantity=4,
            weightinterval=jiDanWeiInt
        )
    def test_search_fanqie_return_corsp_dish_material(self):
        c = Client()
        resp = c.get('/search/', {'search_str': '番茄'})
        resp_json = resp.json()
        dishes = resp_json['dishes']
        self.assertEqual(len(dishes), 3)
        self.assertIn('id', dishes[0])
        self.assertEqual(dishes[0]['name'], '番茄炒蛋')
        self.assertEqual(dishes[0]['estPrice'], 6.5)
        self.assertEqual(dishes[0]['discount'], 1.5)
        self.assertEqual(dishes[0]['like'], 5)
        self.assertIn('id', dishes[1])
        self.assertEqual(dishes[1]['name'], '番茄土豆片')
        self.assertEqual(dishes[1]['estPrice'], 9)
        self.assertEqual(dishes[1]['discount'], 2.5)
        self.assertEqual(dishes[1]['like'], 3)
        self.assertIn('id', dishes[2])
        self.assertEqual(dishes[2]['name'], '(外婆真传)番茄打卤面')
        self.assertEqual(dishes[2]['estPrice'], 9)
        self.assertEqual(dishes[2]['discount'], 2.5)
        self.assertEqual(dishes[2]['like'], 3)
        materials = resp_json['materials']
        self.assertEqual(len(materials), 2)
        self.assertIn('id', materials[0])
        self.assertEqual(materials[0]['name'], '番茄')
        self.assertEqual(materials[0]['breed'], '大红番茄')
        self.assertIn('id', materials[1])
        self.assertEqual(materials[1]['name'], '番茄')
        self.assertEqual(materials[1]['breed'], '粉红番茄')


    def test_return_the_right_dish_detail_giving_dishid(self):
        adish = Dish.objects.get(name__exact= '番茄炒蛋')
        c = Client()
        resp = c.get('/getdishdetail/', {'id': adish.id})
        resp_json = resp.json()
        self.assertIn('id', resp_json)
        resp_json['id'] = 1
        self.assertIn('materials', resp_json)
        self.assertEqual(len(resp_json['materials']), 2)
        self.assertIn('id', resp_json['materials'][0])
        resp_json['materials'][0]['id'] = 1
        self.assertIn('id', resp_json['materials'][1])
        resp_json['materials'][1]['id'] = 1
        exp_json = {
            'id': 1,
            'name': '番茄炒蛋',
            'estPrice': 6.5,
            'discount': 1.5,
            'like': 5,
            'materials': [
                {'id': 1, 'name': '番茄', 'breed': '大红番茄', 'weight': '约0.7kg', 'amount': '2个', 'size': '小', 'supplier': '连贵-蔬菜档'},
                {'id': 1, 'name': '鸡蛋', 'breed': '农家蛋', 'weight': '约1.2kg', 'amount': '4个', 'size': '', 'supplier': '品泰贸易有限公司'}
            ]
        }
        self.assertJSONEqual(str(resp.content, encoding= 'utf8'), exp_json)


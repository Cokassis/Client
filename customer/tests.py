from django.test import TestCase, Client
from random import randint
from customer.models import Customer, HistoryKeyword

# Create your tests here.


class CustomerTestCase(TestCase):
    def setUp(self):
        self.maxDiff = None
        a_customer0 = Customer.objects.create(
            password='123456',
            user_name='sysuye'
        )
        a_customer1 = Customer.objects.create(
            password='123456',
            user_name='weiqing'
        )
        a_customer2 = Customer.objects.create(
            password='123456',
            user_name='zouhy'
        )
        a_customer3 = Customer.objects.create(
            password='123456',
            user_name='wzc'
        )
        a_customer4 = Customer.objects.create(
            password='123456',
            user_name='wfy'
        )
        customer_list = [a_customer0, a_customer1, a_customer2, a_customer3, a_customer4]
        keywords = [
            '番茄炒蛋',
            '酸辣土豆丝',
            '土豆烧牛肉',
            '黑椒牛肉',
            '回锅肉',
            '青瓜炒肉',
            '苦瓜炒蛋',
            '黑椒牛肉',
            '番茄鸡蛋汤',
            '青椒炒鱿鱼'
        ]
        counter = 25
        for a_keyword in keywords:
            HistoryKeyword.objects.create(
                keyword=a_keyword,
                search_count=counter
            ).customers.add(customer_list[randint(0,2)], customer_list[randint(3,4)])
            counter -= 1

    def test_return_five_top_search_dish(self):
        c = Client()
        resp = c.get('/top_search_dish/')
        exp_json = {
            'search_keywords': [
                {
                    'keyword': '番茄炒蛋'
                },
                {
                    'keyword': '酸辣土豆丝'
                },
                {
                    'keyword': '土豆烧牛肉'
                },
                {
                    'keyword': '黑椒牛肉'
                },
                {
                    'keyword': '回锅肉'
                }
            ]
        }
        self.assertJSONEqual(str(resp.content, encoding='utf8'), exp_json)

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def recommend_dish(request):
    result = {
        'dishes': [
            {
                'name': '番茄炒蛋',
                'est_price': 11.5,
                'order_count': 13
            },
            {
                'name': '土豆烧牛肉',
                'est_price': 11.5,
                'order_count': 6
            },
            {
                'name': '黑椒牛肉',
                'est_price': 11.5,
                'order_count': 8
            }
        ]
    }
    return JsonResponse(result)
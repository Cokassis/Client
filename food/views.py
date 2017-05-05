from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def search(request):
    result = {'dishes': [{'name': '番茄炒蛋'}, {'name': '番茄土豆片'}, {'name': '红烧牛肉'}, {'name': '酸辣土豆丝'}, {'name': '糖醋排骨'}],'materials': [{'name': '番茄', 'breed': '大红番茄'}, {'name': '番茄', 'breed': '粉红番茄'}]}
    return JsonResponse(result)
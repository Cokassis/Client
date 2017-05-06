from django.shortcuts import render
from django.http import JsonResponse
from food.models import Dish, Material

# Create your views here.


def search(request):
    if request.method == 'GET':
        search_str = request.GET['search_str']
        dishes = Dish.objects.filter(name__contains= search_str)
        materials = Material.objects.filter(name__contains= search_str)
        dishes_list = []
        for adish in dishes:
            dish_dict = {
                'id': adish.id,
                'name': adish.name,
                'estPrice': adish.estPrice,
                'discount': adish.discount,
                'like': adish.like
            }
            dishes_list.append(dish_dict)
        material_list = []
        for amaterial in materials:
            material_dict = {
                'id': amaterial.id,
                'name': amaterial.name,
                'breed': amaterial.breed
            }
            material_list.append(material_dict)
        result = {
            'dishes': dishes_list,
            'materials': material_list
        }
        return JsonResponse(result)


def getDishDetail(request):
    if request.method == 'GET':
        adish = Dish.objects.get(id__exact= request.GET['id'])
        result = {
            'name': adish.name,
            'estPrice': adish.estPrice,
            'discount': adish.discount,
            'like': adish.like
        }
        return JsonResponse(result)
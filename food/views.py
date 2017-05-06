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
        for dish in dishes:
            dish_dict = {
                'name': dish.name,
                'estPrice': dish.estPrice,
                'discount': dish.discount,
                'like': dish.like
            }
            dishes_list.append(dish_dict)
        material_list = []
        for material in materials:
            material_dict = {
                'name': material.name,
                'breed': material.breed
            }
            material_list.append(material_dict)
        result = {
            'dishes': dishes_list,
            'materials': material_list
        }
        return JsonResponse(result)
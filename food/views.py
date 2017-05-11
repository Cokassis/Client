from django.shortcuts import render
from django.http import JsonResponse
from food.models import Dish, Material, DishMat, WeightInterval
from supplier.models import Supplier

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


def get_dish_detail(request):
    if request.method == 'GET':
        a_dish = Dish.objects.get(id__exact=request.GET['id'])
        materials = a_dish.material_set.all()
        material_list = []
        for a_material in materials:
            a_dish_mat = DishMat.objects.get(dish__id=a_dish.id, material__id=a_material.id)
            a_weight_interval = WeightInterval.objects.get(dishmat=a_dish_mat)
            material_dict = {
                'id': a_material.id,
                'name': a_material.name,
                'breed': a_material.breed,
                'mean_weight': round(a_dish_mat.quantity * (
                    a_weight_interval.intervalMaxWeight +
                    a_weight_interval.intervalMinWeight
                )/2, 2),
                'unit': a_weight_interval.unit,
                'amount': a_dish_mat.quantity,
                'size': a_weight_interval.intervalNote,
                'supplier': DishMat.objects.get(dish=a_dish, material=a_material).supplier.name
            }
            material_list.append(material_dict)
        result = {
            'id': a_dish.id,
            'name': a_dish.name,
            'estPrice': a_dish.estPrice,
            'discount': a_dish.discount,
            'like': a_dish.like,
            'materials': material_list
        }
        return JsonResponse(result)
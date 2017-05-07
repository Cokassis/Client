from django.shortcuts import render
from django.http import JsonResponse
from food.models import Dish, Material, DishMat, WeightInterval

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
        aDish = Dish.objects.get(id__exact= request.GET['id'])
        materials = aDish.material_set.all()
        material_list = []
        for aMaterial in materials:
            aDishMat = DishMat.objects.get(dish__id= aDish.id, material__id= aMaterial.id)
            aWeightInterval = WeightInterval.objects.get(dishmat= aDishMat)
            material_dict = {
                'id': aMaterial.id,
                'name': aMaterial.name,
                'breed': aMaterial.breed,
                'weight': adishmat.quantity * (aWeightInterval.intervalMaxWeight + aWeightInterval.intervalMinWeight)/2,
                'unit': aWeightInterval.unit,
                'amount': adishmat.quantity,
                'size': aWeightInterval.intervalNote,
             #   'supplier':
            }
            material_list.append(material_dict)
        result = {
            'id': adish.id,
            'name': adish.name,
            'estPrice': adish.estPrice,
            'discount': adish.discount,
            'like': adish.like,
            'materials': material_list
        }
        return JsonResponse(result)
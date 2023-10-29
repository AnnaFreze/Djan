from django.shortcuts import render
from django.http import HttpResponse
import requests


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def dish_view(request, dish):
    servings = int(request.GET.get("servings", 1))
    for item in DATA[dish]:
        DATA[dish][item] = DATA[dish][item] * servings
    context = {'recipe': DATA[dish]}
    return render(request, 'calculator/index.html', context)
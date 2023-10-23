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

def omlet_view(request):
    servings = int(request.GET.get("servings", 1))
    for item in DATA['omlet']:
        DATA['omlet'][item] = DATA['omlet'][item] * servings
    context = {'recipe':DATA['omlet']}

    return render(request, 'calculator/index.html', context)

def pasta_view(request):
    servings = int(request.GET.get("servings", 1))
    for item in DATA['pasta']:
        DATA['pasta'][item] = float(DATA['pasta'][item] * servings)
    context = {'recipe':DATA['pasta']}
    return render(request, 'calculator/index.html', context)

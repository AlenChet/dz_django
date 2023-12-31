from django.shortcuts import render
from django.http import HttpResponse

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
def index(request):
    return HttpResponse('Здесь по параметрам запроса выдают рецепт!')
def recipe_view(request, recipe_name):
    servings = request.GET.get('servings', 1)

    try:
        servings = int(servings)
    except ValueError:
        return HttpResponse('Введите число!')

    recipe = DATA.get(recipe_name, {})

    updated_recipe = {}
    for ingredient, quantity in recipe.items():
        updated_quantity = quantity * servings
        updated_recipe[ingredient] = updated_quantity
    context = {
        'recipe': updated_recipe
    }
    return render(request, 'calculator/index.html', context)
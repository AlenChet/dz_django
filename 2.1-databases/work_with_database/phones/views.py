from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    sort_param = request.GET.get('sort')
    phones = Phone.objects.all()

    sort_options = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price',
    }
    phones = phones.order_by(sort_options.get(sort_param, 'name'))
    context = {'phones': phones}
    return render(request, 'catalog.html', context)

def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, 'product.html', context)
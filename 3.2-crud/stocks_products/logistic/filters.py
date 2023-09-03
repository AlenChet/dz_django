import django_filters
from .models import Product, Stock


class ProductFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['search']

class StockFilter(django_filters.FilterSet):
    product = django_filters.CharFilter(field_name='products__product__title', lookup_expr='icontains')


    class Meta:
        model = Stock
        fields = ['product']
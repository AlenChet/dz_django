from rest_framework.viewsets import ModelViewSet
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'title': ['icontains'],
        'description': ['icontains'],
    }
    pagination_class = PageNumberPagination
    page_size = 10


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'products__product__id': ['exact'],
    }
    pagination_class = PageNumberPagination
    page_size = 10
from rest_framework.viewsets import ModelViewSet
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from logistic.filters import ProductFilter, StockFilter
from rest_framework.pagination import PageNumberPagination


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_class = ProductFilter
    pagination_class = PageNumberPagination
    page_size = 10


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_class = StockFilter
    pagination_class = PageNumberPagination
    page_size = 10

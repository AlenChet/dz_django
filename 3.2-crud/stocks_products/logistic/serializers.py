from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from .models import Product, Stock, StockProduct
from .filters import ProductFilter, StockFilter


class ProductSerializer(serializers.ModelSerializer):
    pagination_class = PageNumberPagination
    page_size = 10
    filter_class = ProductFilter
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class StockProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = StockProduct
        fields = ['id', 'product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    products = StockProductSerializer(many=True)
    pagination_class = PageNumberPagination
    page_size = 10
    filter_class = StockFilter

    class Meta:
        model = Stock
        fields = ['id', 'address', 'products']

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        stock = Stock.objects.create(**validated_data)
        for product_data in products_data:
            product = product_data.pop('product')
            stock_product = StockProduct.objects.create(stock=stock, product=product, **product_data)
        return stock

    def update(self, instance, validated_data):
        products_data = validated_data.pop('products')
        instance = super().update(instance, validated_data)

        instance.positions.all().delete()
        for product_data in products_data:
            product = product_data.pop('product')
            stock_product = StockProduct.objects.create(stock=instance, product=product, **product_data)

        return instance

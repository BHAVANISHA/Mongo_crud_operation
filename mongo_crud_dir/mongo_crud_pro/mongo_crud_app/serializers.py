from rest_framework import serializers
from .models import Product


class ProductSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Product
        fields = '__all__'
class Custom1(serializers.Serializer):
    name=serializers.CharField()
    rename_name=serializers.CharField()
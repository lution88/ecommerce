from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Product, ProductImage, ProductOption


class ProductImageSerializer(serializers.ModelSerializer):
    """ 상품 이미지 serializer """
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = ProductImage
        fields = ["image"]


class ProductSerializer(serializers.ModelSerializer):
    """ 상품 serializer """
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "content",
            "price",
            "quantity",
            "region",
            "delivery_method",
            "delivery_charge",
            "images",
        ]

    def get_images(self, obj):
        image = obj.pd_image.all()
        return ProductImageSerializer(
            instance=image,
            many=True,
            context=self.context
        ).data


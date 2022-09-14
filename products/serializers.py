from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Product, ProductImage, ProductOption


class ProductImageSerializer(serializers.ModelSerializer):
    """상품 이미지 serializer"""

    product_image = serializers.ImageField(use_url=True)

    class Meta:
        model = ProductImage
        fields = ["product_image"]


class ProductSerializer(serializers.ModelSerializer):
    """상품 serializer"""

    pd_image = serializers.SerializerMethodField()

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
            "pd_image",
        ]

    def get_pd_image(self, obj):
        pd_image = obj.pd_image.all()
        return ProductImageSerializer(
            instance=pd_image, many=True, context=self.context
        ).data

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        images = self.context["request"].FILES
        for image in images.getlist("pd_image"):
            ProductImage.objects.create(product=product, product_image=image)
        return product

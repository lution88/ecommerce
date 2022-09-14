from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.views import APIView, status
from rest_framework.response import Response

from .models import Product
from .permissions import IsAdminOrReadOnly
from .serializers import ProductSerializer


class ProductsAPIView(APIView):
    """제품리스트 조회 및 생성 API"""

    # 제품 리스트 조회
    def get(self, request):
        products = Product.objects.all()
        product_serializer = ProductSerializer(products, many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)

    # 제품 생성
    def post(self, request):
        product_serializer = ProductSerializer(
            data=request.data, context={"request": request}
        )
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductAPIView(APIView):
    """제품 상세 조회, 수정, 삭제 API"""

    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    # 제품 상세 조회
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        product_serializer = ProductSerializer(product)
        return Response(product_serializer.data, status=status.HTTP_200_OK)

    # 제품 수정
    def put(self, request, product_id):
        product = Product.objects.get(id=product_id)
        product_serializer = ProductSerializer(
            product, data=request.data, partial=True, context={"request": request})
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 제품 삭제
    def delete(self, request, product_id):
        product = Product.objects.get(id=product_id)
        product_serializer = ProductSerializer(product)
        return Response({"message": "delete success!"}, status=status.HTTP_200_OK)

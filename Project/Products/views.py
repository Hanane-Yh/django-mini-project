from django.db.models import Sum
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        ser_data = ProductSerializer(instance=products, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)


class ProductDetail(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        ser_data = ProductSerializer(instance=product)
        return Response(ser_data.data, status=status.HTTP_200_OK)


class ProductCount(APIView):
    def get(self, request):
        total_product_types = Product.objects.count()
        total_count = Product.objects.aggregate(Sum('quantity'))['quantity__sum']
        return Response({'total_product_types': total_product_types, 'total_products': total_count}, status=status.HTTP_200_OK)






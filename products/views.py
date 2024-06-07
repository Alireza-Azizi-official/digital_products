from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, File
from .serializers import CategotrySerializer, ProductSerializer, FileSerializer

class ProductListView(APIView):
    def get(self, request):
        products = products.object.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
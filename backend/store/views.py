from django.shortcuts import render

from store.models import Category, Product
from store.serializers import ProductSerializer, CategorySerializer

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.
class CategoryListView(generics.ListAPIView):
    # ListAPIView so get items for DB so queryset
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny, ]


# Create your views here.
class ProductListView(generics.ListAPIView):
    # ListAPIView so get items for DB so queryset
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny, ]


# One single Item RetriveAPI
class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        slug = self.kwargs['slug']
        return Product.objects.get(slug=slug)
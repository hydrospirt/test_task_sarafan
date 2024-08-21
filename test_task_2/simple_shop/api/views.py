from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from products.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .pagination import StandardResultsSetPagination


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = StandardResultsSetPagination


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

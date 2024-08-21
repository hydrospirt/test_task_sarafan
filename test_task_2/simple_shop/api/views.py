from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from products.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .pagination import StandardResultsSetPagination


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = StandardResultsSetPagination


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

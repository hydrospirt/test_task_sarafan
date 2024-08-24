import logging

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Category, Product

from .pagination import StandardResultsSetPagination
from .serializers import (CartItemSerializer, CartSerializer,
                          CategorySerializer, ProductSerializer)
from .service import Cart

logger = logging.getLogger(__name__)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Предоставляет операцию чтения для модели Category.

    Операции:
    - просмотр списка категорий продуктов с подкатегориями;
    - просмотр конкретной категории по id.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = StandardResultsSetPagination


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Предоставляет операцию чтения для модели Product.

    Операции:
    - просмотр списка продуктов;
    - просмотр конкретного продукта по id.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


class CartAPIView(APIView):
    """
    Предоставляет операции для работы с корзиной.
    """
    permission_classes = (IsAuthenticated, )

    @swagger_auto_schema(
        operation_description="Получить текущую корзину",
        responses={200: CartSerializer()}
    )
    def get(self, request):
        cart = Cart(request)
        logger.debug(f"Session key: {request.session.session_key}")
        return Response(
            {"data": list(cart.__iter__()),
             "cart_total_price": cart.get_total_price()},
            status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Добавить продукт в корзину",
        request_body=CartItemSerializer,
        responses={201: CartItemSerializer()}
    )
    def post(self, request):
        cart = Cart(request)
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.validated_data["product_id"]
            quantity = serializer.validated_data["quantity"]
            logger.debug(f"Adding product {product.id} to cart",
                         f"for session {request.session.session_key}")
            cart = Cart(request)
            cart.add(product, quantity)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Изменить количество продуктов в коризине",
        request_body=CartItemSerializer,
        responses={200: CartItemSerializer()}
    )
    def put(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.validated_data["product_id"]
            quantity = serializer.validated_data["quantity"]
            logger.debug(f"Updating product {product.id} in cart",
                         f" for session {request.session.session_key}")
            cart = Cart(request)
            cart.add(product, quantity, override_quantity=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Удалить продукт из корзины",
        request_body=CartItemSerializer,
        responses={204: "No Content"}
    )
    def delete(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.validated_data["product_id"]
            logger.debug(f"Removing product {product.id} from cart ",
                         f"for session {request.session.session_key}")
            cart = Cart(request)
            cart.remove(product)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClearCartAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Очистить корзину",
        responses={204: "No Content"}
    )
    def delete(self, request):
        logger.debug("Clearing cart for ",
                     f"session {request.session.session_key}")
        cart = Cart(request)
        cart.clear()
        return Response(status=status.HTTP_204_NO_CONTENT)

import logging
from decimal import Decimal

from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication

from products.models import Product

from .serializers import ProductSerializer

logger = logging.getLogger(__name__)


class Cart:
    def __init__(self, request):
        """
        Инициализирует корзину.
        """
        self.session = request.session
        jwt_auth = JWTAuthentication()
        user, _ = jwt_auth.authenticate(request)
        self.user_id = str(user.id) if user else None
        cart = self.session.get(settings.CART_SESSION_ID,
                                {}).get(self.user_id, {})
        if not cart:
            self.session.setdefault(settings.CART_SESSION_ID,
                                    {})[self.user_id] = {}
        self.cart = self.session[settings.CART_SESSION_ID][self.user_id]

        logger.info(f"Session ID: {self.user_id}, Cart: {self.cart}")

    def save(self):
        self.session.modified = True

    def add(self, product, quantity=1, override_quantity=False):
        """
        Добавить товар в корзину или обновить его количество
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0,
                "price": str(product.price)
            }
        if override_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity
        self.save()

    def remove(self, product):
        """
        Удалить товар из корзины
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Просмотреть товары в корзине и извлечь их из базы данных.
        """
        product_ids = [key for key in self.cart.keys()
                       if key not in ["quantity", "price"]]
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]["product"] = ProductSerializer(product).data
        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        """
        Подсчитать все товары в корзине.
        """
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item["price"])
                   * item["quantity"] for item in self.cart.values())

    def clear(self):
        """
        Очистка корзины из сессии.
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()

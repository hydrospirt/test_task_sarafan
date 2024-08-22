from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ProductViewSet, CartAPIView, ClearCartAPIView

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"products", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("cart/", CartAPIView.as_view(), name="cart"),
    path("cart/clear/", ClearCartAPIView.as_view(), name="cart-clear"),
]

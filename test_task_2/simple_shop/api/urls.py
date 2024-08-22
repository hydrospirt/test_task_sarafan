from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (CartAPIView, CategoryViewSet, ClearCartAPIView,
                    ProductViewSet)


router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"products", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("cart/", CartAPIView.as_view(), name="cart"),
    path("cart/clear/", ClearCartAPIView.as_view(), name="cart-clear"),
]

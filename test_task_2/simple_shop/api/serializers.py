from django.conf import settings
from rest_framework import serializers
from rest_framework.request import Request

from api.utils import extract_media_path
from products.models import Category, Product, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ("id", "name", "slug", "image")


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("id", "name", "slug", "image", "subcategories")


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="slug",
                                            read_only=True)
    subcategory = serializers.SlugRelatedField(slug_field="slug",
                                               read_only=True)
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("id", "name", "slug", "category",
                  "subcategory", "price", "images")

    def get_images(self, obj):
        request = self.context.get('request')
        if not isinstance(request, Request):
            return {}
        base_url = request.build_absolute_uri(settings.MEDIA_URL)
        images = {
            "original": (base_url
                         + extract_media_path(obj.image_original.url)
                         if obj.image_original else None),
            "small": (base_url
                      + extract_media_path(obj.image_small.url)
                      if obj.image_small else None),
            "medium": (base_url
                       + extract_media_path(obj.image_medium.url)
                       if obj.image_medium else None),
        }
        return images


class CartItemSerializer(serializers.Serializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all())
    quantity = serializers.IntegerField(min_value=1)


class CartSerializer(serializers.Serializer):
    items = CartItemSerializer(many=True)

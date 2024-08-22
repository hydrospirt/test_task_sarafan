from rest_framework import serializers
from products.models import Category, SubCategory, Product


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
        images = {
            "original": obj.image.url if obj.image else None,
            "small": obj.image_small.url if obj.image_small else None,
            "medium": obj.image_medium.url if obj.image_medium else None,
            "large": obj.image_large.url if obj.image_large else None,
        }
        return images


class CartItemSerializer(serializers.Serializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all())
    quantity = serializers.IntegerField(min_value=1)


class CartSerializer(serializers.Serializer):
    items = CartItemSerializer(many=True)

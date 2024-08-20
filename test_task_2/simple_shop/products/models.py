from django.db import models
from PIL import Image
import os


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=15, unique=True)
    image = models.ImageField(upload_to="categories/",
                              null=True, blank=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=15, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="categories/sub_categories/",
                              null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory,
                                    on_delete=models.SET_NULL,
                                    null=True, blank=True)
    image = models.ImageField(upload_to="products/",
                              null=True, blank=True)
    image_small = models.ImageField(upload_to="products/",
                                    null=True, blank=True)
    image_medium = models.ImageField(upload_to="products/",
                                     null=True, blank=True)
    image_large = models.ImageField(upload_to="products/",
                                    null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            self.create_thumbnails()

    def create_thumbnails(self, *args, **kwargs):
        img = Image.open(self.image.path)

        sizes = {
            "small": (100, 100),
            "medium": (300, 300),
            "large": (600, 600),
        }

        for size_name, size in sizes.items():
            img_copy = img.copy()
            img_copy.thumbnail(size)
            thumb_nail_path = os.path.join(
                os.path.dirname(self.image.path),
                f"{os.path.basename(self.image.name).split(".")[0]}_"
                + f"{size_name}.{self.image.name.split(".")[-1]}"
            )
            img_copy.save(thumb_nail_path)

            setattr(self, f"image_{size_name}", thumb_nail_path)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

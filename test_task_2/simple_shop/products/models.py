from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify
from PIL import Image
import os


def generic_image_path(instance, filename):
    model_name = instance._meta.model_name
    date_time = now().strftime("%Y-%m-%d")
    extension = filename.split('.')[-1]
    new_filename = f"{instance.slug}.{extension}"
    return os.path.join(model_name, date_time, new_filename)


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=15, unique=True)
    image = models.ImageField(upload_to=generic_image_path,
                              null=True, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("-id", )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=15, unique=True)
    category = models.ForeignKey(Category, related_name="subcategories",
                                 on_delete=models.CASCADE)
    image = models.ImageField(upload_to=generic_image_path,
                              null=True, blank=True)

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        ordering = ("-id", )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    slug = models.SlugField(max_length=15, unique=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory,
                                    on_delete=models.SET_NULL,
                                    null=True, blank=True)
    image = models.ImageField(upload_to=generic_image_path,
                              null=True, blank=True)
    image_small = models.ImageField(upload_to=generic_image_path,
                                    null=True, blank=True)
    image_medium = models.ImageField(upload_to=generic_image_path,
                                     null=True, blank=True)
    image_large = models.ImageField(upload_to=generic_image_path,
                                    null=True, blank=True)
    is_available = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("-id", )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.name)

        if self.quantity == 0:
            self.is_available = False
        else:
            self.is_available = True

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

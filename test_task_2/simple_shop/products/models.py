import os

from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from PIL import Image


def generic_image_path(instance, filename):
    model_name = instance._meta.model_name
    date = now().strftime("%Y-%m-%d")
    extension = filename.split('.')[-1]
    new_filename = f"{instance.slug}.{extension}"
    return os.path.join(model_name, date, new_filename)


class Category(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Название")
    slug = models.SlugField(max_length=15,
                            verbose_name="URL-slug",
                            unique=True)
    image = models.ImageField(upload_to=generic_image_path,
                              verbose_name="Изображение",
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
    name = models.CharField(max_length=100,
                            verbose_name="Название")
    slug = models.SlugField(max_length=15,
                            verbose_name="URL-slug",
                            unique=True)
    category = models.ForeignKey(Category, related_name="subcategories",
                                 verbose_name="Категория",
                                 on_delete=models.CASCADE)
    image = models.ImageField(upload_to=generic_image_path,
                              verbose_name="Изображение",
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
    name = models.CharField(max_length=100,
                            verbose_name="Название",)
    price = models.DecimalField(max_digits=10,
                                verbose_name="Цена",
                                decimal_places=2)
    description = models.TextField(verbose_name="Описание",)
    slug = models.SlugField(max_length=15,
                            verbose_name="URL-slug",
                            unique=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 verbose_name="Категория",
                                 null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory,
                                    on_delete=models.SET_NULL,
                                    verbose_name="Подкатегория",
                                    null=True, blank=True)
    image_original = models.ImageField(upload_to=generic_image_path,
                                       verbose_name="Изображение",
                                       null=True, blank=True)
    image_small = models.ImageField(upload_to=generic_image_path,
                                    verbose_name="Значек",
                                    null=True, blank=True)
    image_medium = models.ImageField(upload_to=generic_image_path,
                                     verbose_name="Превью",
                                     null=True, blank=True)
    is_available = models.BooleanField(default=True,
                                       verbose_name="В наличии",)
    quantity = models.PositiveIntegerField(default=1,
                                           verbose_name="Количество",)

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

        if self.image_original:
            self.create_thumbnails()

    def create_thumbnails(self, *args, **kwargs):
        img = Image.open(self.image_original.path)

        sizes = {
            "small": (100, 100),
            "medium": (300, 300),
        }

        for size_name, size in sizes.items():
            img_copy = img.copy()
            img_copy.thumbnail(size)
            thumb_nail_path = os.path.join(
                os.path.dirname(self.image_original.path),
                f"{os.path.basename(self.image_original.name).split(".")[0]}_"
                + f"{size_name}.{self.image_original.name.split(".")[-1]}"
            )
            img_copy.save(thumb_nail_path)
            setattr(self, f"image_{size_name}", thumb_nail_path)
        super().save(*args, **kwargs)

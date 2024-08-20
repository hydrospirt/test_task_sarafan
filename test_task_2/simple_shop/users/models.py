from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = PhoneNumberField(
        unique=True,
        null=False,
        blank=False)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username", )

    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        help_text="Группы, к которым принадлежит этот пользователь.",
        related_name="customuser_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        help_text="Определенные разрешения для этого пользователя.",
        related_name="customuser_set",
        related_query_name="user",
    )

    def __str__(self):
        return self.username

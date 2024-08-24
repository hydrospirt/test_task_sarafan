from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30,
                                  verbose_name="Имя",
                                  blank=True)
    last_name = models.CharField(max_length=30,
                                 verbose_name="Фамилия",
                                 blank=True)
    phone_number = PhoneNumberField(
        verbose_name="Номер телефона",
        unique=True,
        null=False,
        blank=False)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username", )

    groups = models.ManyToManyField(
        Group,
        verbose_name="группы",
        blank=True,
        help_text="Группы, к которым принадлежит этот пользователь.",
        related_name="customuser_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="права пользователя",
        blank=True,
        help_text="Определенные разрешения для этого пользователя.",
        related_name="customuser_set",
        related_query_name="user",
    )

    def __str__(self):
        return self.username

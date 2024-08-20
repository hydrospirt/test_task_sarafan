from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "email"
                    "phone_number",
                    "role",
                    "is_active",
                    "is_staff")

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    list_display = ("id", "email", "username",
                    "phone_number", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name",
                                      "last_name",
                                      "phone_number")}),
        ("Permissions", {"fields": (
            "is_active", "is_staff",
            "is_superuser", "groups",
            "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username",
                       "phone_number", "password1", "password2"),
        }),
    )
    search_fields = ("email", "username", "phone_number")
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)

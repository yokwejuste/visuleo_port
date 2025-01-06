from django.contrib import admin

from unfold.admin import ModelAdmin
from .models import UserTag, VisuleoUser

admin.site.register(UserTag)


@admin.register(VisuleoUser)
class VisuleoUserAdmin(ModelAdmin):
    list_display = ("email", "name", "is_active", "is_staff", "is_superuser")
    list_filter = ("is_active", "is_staff", "is_superuser")
    search_fields = ("email", "name", "username")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("name", "phone_number")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
        }),
    )
    readonly_fields = ("last_login", "date_joined")
    filter_horizontal = ()


admin.site.site_header = "Visuleo Admin"
admin.site.site_title = "Visuleo Admin Portal"
admin.site.index_title = "Welcome to Visuleo Portal"

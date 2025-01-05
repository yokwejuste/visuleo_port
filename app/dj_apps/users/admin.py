from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Client, UserTag, Domain


@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ("name", "paid_until")


admin.site.register(UserTag)
admin.site.register(Domain)

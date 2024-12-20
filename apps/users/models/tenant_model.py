from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    subdomain = models.CharField(max_length=100, unique=True)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True
    auto_drop_schema = True

    def __str__(self) -> str:
        return str(self.name)
    
    class Meta:
        db_table = 'clients'


class Domain(DomainMixin):
    pass

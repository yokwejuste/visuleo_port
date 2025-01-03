from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django_tenants.utils import get_tenant_model


class Command(BaseCommand):
    help = 'Resets the tenant database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--tenants',
            nargs='+',
            help='Specify one or more tenant names, or "all" to reset all tenants'
        )

    def handle(self, *args, **options):
        tenants = options['tenants']
        if not tenants:
            raise CommandError("No tenants specified. Use --tenants followed by tenant names or 'all'.")

        if 'all' in tenants:
            if len(tenants) > 1:
                raise CommandError("When using 'all', do not specify individual tenants.")
            self.reset_all_tenants()
        else:
            for tenant_name in tenants:
                self.reset_tenant(tenant_name)

        self.stdout.write(self.style.SUCCESS('Requested tenant(s) reset successfully!'))

    def reset_all_tenants(self):
        tenant_model = get_tenant_model()
        for tenant in tenant_model.objects.all():
            self.reset_tenant_schema(tenant)

    def reset_tenant(self, tenant_name):
        tenant_model = get_tenant_model()
        try:
            tenant = tenant_model.objects.get(schema_name=tenant_name)
            self.reset_tenant_schema(tenant)
        except tenant_model.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Tenant "{tenant_name}" does not exist.'))

    def reset_tenant_schema(self, tenant):
        with connection.cursor() as cursor:
            cursor.execute(f"DROP SCHEMA IF EXISTS {tenant.schema_name} CASCADE;")
            cursor.execute(f"CREATE SCHEMA {tenant.schema_name};")
            self.stdout.write(self.style.SUCCESS(f'Tenant "{tenant.schema_name}" reset successfully.'))

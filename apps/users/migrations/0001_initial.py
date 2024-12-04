# Generated by Django 5.0.1 on 2024-11-25 22:33

import django.db.models.deletion
import django.utils.timezone
import django_tenants.postgresql_backend.base
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_name', models.CharField(db_index=True, max_length=63, unique=True, validators=[django_tenants.postgresql_backend.base._check_schema_name])),
                ('name', models.CharField(max_length=100)),
                ('subdomain', models.CharField(max_length=100, unique=True)),
                ('paid_until', models.DateField()),
                ('on_trial', models.BooleanField()),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'clients',
            },
        ),
        migrations.CreateModel(
            name='VisuleoUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.AutoField(editable=False, help_text='Unique identifier for this object.', primary_key=True, serialize=False, verbose_name='id')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date and time when this object was created.', verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date and time when this object was last updated.', verbose_name='updated')),
                ('is_deleted', models.BooleanField(default=False, help_text='Boolean field to mark if this object is deleted.', verbose_name='is deleted')),
                ('name', models.CharField(blank=True, help_text="User's full name.", max_length=255, verbose_name='name')),
                ('email', models.EmailField(help_text="User's email address.", max_length=254, unique=True, verbose_name='email address')),
                ('phone_number', models.CharField(blank=True, help_text="User's phone number.", max_length=20, verbose_name='phone number')),
                ('email_verified', models.BooleanField(default=False, help_text="Boolean field to mark if this user's email is verified.", verbose_name='is email verified')),
                ('phone_number_verified', models.BooleanField(default=False, help_text="Boolean field to mark if this user's phone number is verified.", verbose_name='is phone number verified')),
                ('is_active', models.BooleanField(default=True, help_text='Boolean field to mark if this user is active.', verbose_name='is active')),
                ('is_superuser', models.BooleanField(default=False, help_text='Boolean field to mark if this user is superuser.', verbose_name='is superuser')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, help_text='Date and time when this user last logged in.', verbose_name='last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, help_text='Date and time when this user joined.', verbose_name='date joined')),
                ('created_by', models.ForeignKey(blank=True, help_text='User who created this object.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, help_text='User who last updated this object.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'users',
                'ordering': ('-created', '-updated'),
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(db_index=True, max_length=253, unique=True)),
                ('is_primary', models.BooleanField(db_index=True, default=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domains', to='users.client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserTag',
            fields=[
                ('id', models.AutoField(editable=False, help_text='Unique identifier for this object.', primary_key=True, serialize=False, verbose_name='id')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date and time when this object was created.', verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date and time when this object was last updated.', verbose_name='updated')),
                ('is_deleted', models.BooleanField(default=False, help_text='Boolean field to mark if this object is deleted.', verbose_name='is deleted')),
                ('name', models.CharField(help_text='Name of the user type.', max_length=255, verbose_name='name')),
                ('created_by', models.ForeignKey(blank=True, help_text='User who created this object.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, help_text='User who last updated this object.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user type',
                'verbose_name_plural': 'user types',
                'db_table': 'user_tags',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='visuleouser',
            name='user_tag',
            field=models.ManyToManyField(help_text='User tag for the user.', related_name='users', to='users.usertag', verbose_name='user tag'),
        ),
    ]

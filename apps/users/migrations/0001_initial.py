# Generated by Django 5.0.1 on 2024-01-24 18:24

import django.db.models.deletion
import django.utils.timezone
import django_tenants.postgresql_backend.base
import utils.main
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_name', models.CharField(db_index=True, max_length=63, unique=True, validators=[django_tenants.postgresql_backend.base._check_schema_name])),
                ('name', models.CharField(max_length=100)),
                ('subdomain', models.CharField(max_length=100, unique=True)),
                ('paid_until', models.DateField()),
                ('on_trial', models.BooleanField()),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the user type.', max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'user type',
                'verbose_name_plural': 'user types',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(db_index=True, max_length=253, unique=True)),
                ('is_primary', models.BooleanField(db_index=True, default=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domains', to='users.client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VisuleoUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.UUIDField(default=utils.main.generate_uuid, editable=False, help_text='Unique identifier for this object.', primary_key=True, serialize=False, verbose_name='id')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date and time when this object was created.', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date and time when this object was last modified.', verbose_name='modified')),
                ('is_deleted', models.BooleanField(default=False, help_text='Boolean field to mark if this object is deleted.', verbose_name='is deleted')),
                ('name', models.CharField(blank=True, help_text="User's full name.", max_length=255, verbose_name='name')),
                ('email', models.EmailField(help_text="User's email address.", max_length=254, unique=True, verbose_name='email address')),
                ('phone_number', models.CharField(blank=True, help_text="User's phone number.", max_length=20, verbose_name='phone number')),
                ('is_email_verified', models.BooleanField(default=False, help_text="Boolean field to mark if this user's email is verified.", verbose_name='is email verified')),
                ('is_phone_number_verified', models.BooleanField(default=False, help_text="Boolean field to mark if this user's phone number is verified.", verbose_name='is phone number verified')),
                ('is_active', models.BooleanField(default=True, help_text='Boolean field to mark if this user is active.', verbose_name='is active')),
                ('is_superuser', models.BooleanField(default=False, help_text='Boolean field to mark if this user is superuser.', verbose_name='is superuser')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, help_text='Date and time when this user last logged in.', verbose_name='last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, help_text='Date and time when this user joined.', verbose_name='date joined')),
                ('user_tag', models.ManyToManyField(help_text='User tag for the user.', related_name='users', to='users.usertag', verbose_name='user tag')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ('-created', '-modified'),
            },
        ),
    ]

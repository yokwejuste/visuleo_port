# Generated by Django 4.1.7 on 2023-11-26 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visuleouser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='visuleouser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='visuleouser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='visuleouser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='visuleouser',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='visuleouser',
            name='username',
        ),
    ]

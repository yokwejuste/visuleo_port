# Generated by Django 4.1.7 on 2023-07-30 16:31

from django.db import migrations, models
import utils.main


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.UUIDField(default=utils.main.generate_uuid, editable=False, help_text='Unique identifier for this object.', primary_key=True, serialize=False, verbose_name='id')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date and time when this object was created.', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date and time when this object was last modified.', verbose_name='modified')),
                ('is_deleted', models.BooleanField(default=False, help_text='Boolean field to mark if this object is deleted.', verbose_name='is deleted')),
                ('name', models.CharField(help_text='Name of the category.', max_length=255, verbose_name='name')),
                ('description', models.TextField(help_text='Description of the category.', verbose_name='description')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.UUIDField(default=utils.main.generate_uuid, editable=False, help_text='Unique identifier for this object.', primary_key=True, serialize=False, verbose_name='id')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date and time when this object was created.', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date and time when this object was last modified.', verbose_name='modified')),
                ('is_deleted', models.BooleanField(default=False, help_text='Boolean field to mark if this object is deleted.', verbose_name='is deleted')),
                ('name', models.CharField(help_text='Name of the project.', max_length=255, verbose_name='name')),
                ('slug', models.SlugField(help_text='Slug for the project.', max_length=255, unique=True, verbose_name='slug')),
                ('description', models.TextField(help_text='Description of the project.', verbose_name='description')),
                ('image', models.ImageField(help_text='Image for the project.', upload_to='projects/', verbose_name='image')),
                ('url', models.URLField(help_text='URL for the project.', max_length=255, verbose_name='url')),
                ('is_featured', models.BooleanField(default=False, help_text='Boolean field to mark if this project is featured.', verbose_name='is featured')),
                ('categories', models.ManyToManyField(help_text='Categories for the project.', related_name='projects', to='portfolio.categories', verbose_name='categories')),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
            },
        ),
    ]

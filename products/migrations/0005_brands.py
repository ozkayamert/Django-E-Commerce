# Generated by Django 5.1.3 on 2024-11-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_categories_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('description', models.TextField(blank=True, null=True)),
                ('seo_title', models.CharField(blank=True, max_length=155, null=True)),
                ('seo_description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=155, null=True, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='brand-pictures')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
    ]
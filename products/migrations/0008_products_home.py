# Generated by Django 5.1.3 on 2024-11-20 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_tags_products_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='home',
            field=models.BooleanField(default=False),
        ),
    ]
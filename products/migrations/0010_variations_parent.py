# Generated by Django 5.1.3 on 2024-11-25 10:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_variations'),
    ]

    operations = [
        migrations.AddField(
            model_name='variations',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.variations'),
        ),
    ]

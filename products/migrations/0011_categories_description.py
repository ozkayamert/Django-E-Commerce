# Generated by Django 5.1.3 on 2024-11-26 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_variations_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

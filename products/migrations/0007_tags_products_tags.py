# Generated by Django 5.1.3 on 2024-11-19 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('slug', models.SlugField(blank=True, max_length=155, null=True, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='products',
            name='tags',
            field=models.ManyToManyField(blank=True, to='products.tags'),
        ),
    ]
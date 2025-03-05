# Generated by Django 5.1.1 on 2025-01-29 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0011_cart'),
        ('vendor', '0002_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image', models.ImageField(help_text='Upload the banner image', upload_to='banner_image')),
                ('description', models.TextField(blank=True, help_text='Short description of the offer', null=True)),
                ('is_active', models.BooleanField(default=True, help_text='only active banners will be displayed')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_banner_products', to='productsapp.products')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_banner', to='vendor.vendors')),
            ],
        ),
    ]

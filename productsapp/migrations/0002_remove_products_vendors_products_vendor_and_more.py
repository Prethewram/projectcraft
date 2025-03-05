# Generated by Django 5.1.1 on 2025-01-25 05:49

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0001_initial'),
        ('vendor', '0002_delete_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='vendors',
        ),
        migrations.AddField(
            model_name='products',
            name='vendor',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='vendor.vendors'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='Popular_products',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='discount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='isofferproduct',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='newarrival',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='products',
            name='trending_one',
            field=models.BooleanField(default=False),
        ),
    ]

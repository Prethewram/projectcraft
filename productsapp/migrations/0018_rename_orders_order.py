# Generated by Django 5.1.4 on 2025-02-19 07:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("productsapp", "0017_rename_order_orders"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Orders",
            new_name="Order",
        ),
    ]

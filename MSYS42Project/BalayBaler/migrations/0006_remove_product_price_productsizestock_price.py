# Generated by Django 4.2.16 on 2024-09-17 09:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("BalayBaler", "0005_size_remove_product_size_alter_product_image_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="price",
        ),
        migrations.AddField(
            model_name="productsizestock",
            name="price",
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10),
            preserve_default=False,
        ),
    ]

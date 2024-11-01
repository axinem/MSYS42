# Generated by Django 4.2.16 on 2024-10-24 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("BalayBaler", "0007_customer_date_created"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name="Customer",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="session_key",
        ),
        migrations.RemoveField(
            model_name="cartitem",
            name="session_key",
        ),
        migrations.RemoveField(
            model_name="product",
            name="available_sizes",
        ),
        migrations.AddField(
            model_name="cart",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="cartitem",
            name="size",
            field=models.CharField(default="100g", max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="price_100g",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="product",
            name="price_4L",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="product",
            name="price_6L",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="product",
            name="stock_100g",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="product",
            name="stock_4L",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="product",
            name="stock_6L",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="cart",
            name="items",
            field=models.ManyToManyField(blank=True, to="BalayBaler.cartitem"),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name="ProductSizeStock",
        ),
        migrations.DeleteModel(
            name="Size",
        ),
    ]

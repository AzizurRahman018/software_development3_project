# Generated by Django 4.2.7 on 2023-11-14 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop_app", "0001_initial"),
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
                ("title", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="ClothingMaterial",
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
                ("title", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="COLOR",
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
                ("title", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="CONDITION",
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
                ("title", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="SIZE",
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
                ("title", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Slider",
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
                ("title", models.CharField(max_length=50)),
                ("title1", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("button_tag", models.CharField(max_length=20)),
                ("image", models.ImageField(upload_to="slider_image/")),
            ],
        ),
        migrations.CreateModel(
            name="SubCategory",
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
                ("title", models.CharField(max_length=50)),
                (
                    "Catagory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop_app.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Super_SubCategory",
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
                ("title", models.CharField(max_length=50)),
                (
                    "SubCategory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop_app.subcategory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=20)),
                ("image", models.ImageField(upload_to="Product_image/")),
                (
                    "image1",
                    models.ImageField(
                        blank=True, null=True, upload_to="Product_image1/"
                    ),
                ),
                (
                    "image2",
                    models.ImageField(
                        blank=True, null=True, upload_to="Product_image2/"
                    ),
                ),
                (
                    "image3",
                    models.ImageField(
                        blank=True, null=True, upload_to="Product_image3/"
                    ),
                ),
                ("current_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("prev_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("short_description", models.TextField()),
                ("top_seller", models.BooleanField(default=False)),
                ("deals_of_the_day", models.BooleanField(default=False)),
                ("trending_product", models.BooleanField(default=False)),
                ("featured_product", models.BooleanField(default=False)),
                ("quantity", models.PositiveIntegerField()),
                ("wish_list", models.BooleanField(default=False)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "Clothing_Material",
                    models.ManyToManyField(to="shop_app.clothingmaterial"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop_app.category",
                    ),
                ),
                ("color", models.ManyToManyField(to="shop_app.color")),
                ("condition", models.ManyToManyField(to="shop_app.condition")),
                (
                    "posted_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("size", models.ManyToManyField(to="shop_app.size")),
                (
                    "sub_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop_app.subcategory",
                    ),
                ),
                (
                    "super_sub_Category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop_app.super_subcategory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cart",
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
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop_app.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-19 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shop_app", "0001_initial"),
    ]

    operations = [
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
        migrations.AddField(
            model_name="product",
            name="super_sub_Category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop_app.super_subcategory",
            ),
        ),
    ]
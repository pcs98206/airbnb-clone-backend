# Generated by Django 4.1.7 on 2023-03-27 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0002_alter_category_options"),
        ("experiences", "0002_rename_explantion_perk_explanation"),
    ]

    operations = [
        migrations.AddField(
            model_name="experience",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="categories.category",
            ),
        ),
    ]

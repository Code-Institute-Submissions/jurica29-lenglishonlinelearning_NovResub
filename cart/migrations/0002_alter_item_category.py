# Generated by Django 4.1 on 2022-10-17 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.CharField(
                choices=[("L", "Lesson"), ("C", "Course")], max_length=5
            ),
        ),
    ]

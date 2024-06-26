# Generated by Django 5.0.4 on 2024-04-24 20:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts_app", "0002_posts_opinions"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("nome", models.CharField(max_length=100)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Category",
                "ordering": ["id"],
            },
        ),
        migrations.AddField(
            model_name="posts",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="posts_app.category",
            ),
        ),
    ]

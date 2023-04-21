# Generated by Django 4.2 on 2023-04-21 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0005_delete_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("body", models.CharField(max_length=500, null=True)),
                ("time", models.DateTimeField(auto_now_add=True)),
                ("user", models.CharField(max_length=50, null=True)),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="pages.match",
                    ),
                ),
            ],
            options={
                "ordering": ("time",),
            },
        ),
    ]

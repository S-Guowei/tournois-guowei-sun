# Generated by Django 4.2 on 2023-04-21 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0003_comment"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Comment",
        ),
    ]

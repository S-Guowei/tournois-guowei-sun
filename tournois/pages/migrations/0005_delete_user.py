# Generated by Django 4.2 on 2023-04-21 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0004_delete_comment"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]

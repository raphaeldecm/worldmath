# Generated by Django 4.2 on 2023-12-15 17:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_userprofile"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]
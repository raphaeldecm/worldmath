# Generated by Django 4.2 on 2023-05-23 23:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="exercicios",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("conteudo", models.CharField(max_length=150)),
                ("tipo", models.TextField()),
                ("download", models.TextField()),
            ],
        ),
    ]

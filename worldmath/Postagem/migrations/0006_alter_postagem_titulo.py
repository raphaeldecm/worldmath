# Generated by Django 4.2 on 2023-12-15 16:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Postagem", "0005_alter_postagem_resumo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postagem",
            name="titulo",
            field=models.CharField(max_length=100),
        ),
    ]
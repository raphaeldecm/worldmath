# Generated by Django 4.2 on 2023-12-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Postagem", "0002_mensagemcontato"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postagem",
            name="Resumo",
            field=models.CharField(blank=True, null=True, verbose_name=200),
        ),
        migrations.AlterField(
            model_name="postagem",
            name="titulo",
            field=models.CharField(max_length=200),
        ),
    ]
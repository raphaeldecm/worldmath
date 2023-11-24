# Generated by Django 4.2 on 2023-11-24 18:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Postagem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Created at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated at")),
                ("titulo", models.CharField(max_length=100)),
                ("Texto", models.TextField(blank=True, null=True)),
                ("imagem", models.ImageField(blank=True, null=True, upload_to="imagens")),
                ("Resumo", models.CharField(blank=True, max_length=255, null=True)),
                ("conteudo", models.CharField(blank=True, max_length=100, null=True)),
                ("tipo_arquivo", models.CharField(blank=True, max_length=50, null=True)),
                ("Url", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "categoria_postagem",
                    models.CharField(
                        choices=[
                            ("Matematicos", "Matematicos"),
                            ("Novidades", "Novidades"),
                            ("Historia", "Historia"),
                            ("Exercicios", "Exercicios"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]

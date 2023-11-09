from django.db import models
from django.utils.translation import gettext_lazy as _

from core.constants import (MAX_CHAR_FIELD_NAME_LENGTH,
                            MEDIUM_CHAR_FIELD_NAME_LENGTH,
                            SMALL_CHAR_FIELD_NAME_LENGTH)

# Create your models here.
class Matematicos(models.Model):
    imagem = models.ImageField(upload_to='imagens')
    Resumo = models.CharField(max_length=300)

    
    def __str__(self):
        return self.titulo

class Poesias(models.Model):
    Autor = models.CharField(max_length=150)

    def __str__(self):
        return self.Autor

class Historia(models.Model):

    def __str__(self):
        return self.titulo

class Exercicios(models.Model):
    conteudo = models.CharField(max_length=150)
    tipo_arquivo = models.CharField(max_length=30)
    Url = models.CharField(max_length=150)

    def __str__(self):
        return self.conteudo

class Postagem(models.Model):
    TITULO_CHOICES = (
        ('exercicios', 'Exercícios'),
        ('matematicos', 'Matemáticos'),
        ('poesias', 'Poesias'),
        ('historia', 'História'),
    )

    titulo = models.CharField(max_length=150)
    Data_postagem = models.DateField()
    Texto = models.TextField()
    matematicos = models.ForeignKey(Matematicos, on_delete=models.CASCADE, null=True, blank=True)
    tipo = models.CharField(max_length=30, choices=TITULO_CHOICES)

    def __str__(self):
        return self.titulo


from django.db import models
from django.utils.translation import gettext_lazy as _

from core.constants import (MAX_CHAR_FIELD_NAME_LENGTH,
                            MEDIUM_CHAR_FIELD_NAME_LENGTH,
                            SMALL_CHAR_FIELD_NAME_LENGTH)
from core.models import BaseModel

class Postagem(BaseModel):
    CATEGORIAS = [
        ('Matematicos', 'Matematicos'),
        ('Novidades', 'Novidades'),  
        ('Historia', 'Historia'),
        ('Exercicios', 'Exercicios'),
    ]

    titulo = models.CharField(max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH)
    Data_postagem = models.DateField()
    Texto = models.TextField()
    imagem = models.ImageField(upload_to='imagens', null=True)
    Resumo = models.CharField(max_length=MAX_CHAR_FIELD_NAME_LENGTH, null=True)
    conteudo = models.CharField(max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH, null=True)
    tipo_arquivo = models.CharField(max_length=SMALL_CHAR_FIELD_NAME_LENGTH, null=True)
    Url = models.CharField(max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH, null=True)
    categoria_postagem = models.CharField(max_length=SMALL_CHAR_FIELD_NAME_LENGTH, choices=CATEGORIAS)

    def __str__(self):
        return self.categoria
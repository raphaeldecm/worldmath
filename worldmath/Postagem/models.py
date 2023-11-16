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
    imagem = models.ImageField(upload_to='imagens')
    Resumo = models.CharField(max_length=MAX_CHAR_FIELD_NAME_LENGTH)
    conteudo = models.CharField(max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH)
    tipo_arquivo = models.CharField(max_length=SMALL_CHAR_FIELD_NAME_LENGTH)
    Url = models.CharField(max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH)
    categoria_postagem = models.CharField(max_length=SMALL_CHAR_FIELD_NAME_LENGTH, choices=CATEGORIAS)

    def __str__(self):
        return self.titulo

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.constants import (MAX_CHAR_FIELD_NAME_LENGTH,
                            MEDIUM_CHAR_FIELD_NAME_LENGTH,
                            SMALL_CHAR_FIELD_NAME_LENGTH)
from core.models import BaseModel


# Create your models here.
class Matematicos(BaseModel):
    imagem = models.ImageField(upload_to='imagens')
    Resumo = models.CharField(max_length=MAX_CHAR_FIELD_NAME_LENGTH)

class Historia(BaseModel):
    imagem = models.ImageField(upload_to='imagens')

class Exercicios(BaseModel):
    conteudo = models.CharField(max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH)
    tipo_arquivo = models.CharField(max_length=SMALL_CHAR_FIELD_NAME_LENGTH)
    Url = models.CharField(max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH)

    def __str__(self):
        return self.conteudo
    
class Diversidades(BaseModel):
    class CategoriaDiversidades(models.TextChoices):
        Enem = "Enem", _("Enem")
        Novidades = "Novidades", _("Novidades")

    imagem = models.ImageField(upload_to='imagens')
    categoria_diversidades = models.CharField(max_length=SMALL_CHAR_FIELD_NAME_LENGTH, choices=CategoriaDiversidades.choices,)    


class Postagem(BaseModel):
    class CategoriaPostagem(models.TextChoices):
        Exercicios = "Exercicios", _("Exercicios")
        Matematicos = "Matematicos", _("Matematicos")
        Historia = "Historia", _("Historia")
        Diversidades = "Diversidades", _("Diversidades")

    titulo = models.CharField(max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH)
    Data_postagem = models.DateField()
    Texto = models.TextField()
    categoria_postagem = models.CharField(max_length=SMALL_CHAR_FIELD_NAME_LENGTH, choices=CategoriaPostagem.choices,)


    def __str__(self):
        return self.titulo
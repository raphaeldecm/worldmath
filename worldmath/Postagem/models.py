from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from core.constants import (MAX_CHAR_FIELD_NAME_LENGTH, MEDIUM_CHAR_FIELD_NAME_LENGTH, SMALL_CHAR_FIELD_NAME_LENGTH)
from core.models import BaseModel
from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _

class Postagem(BaseModel):
    CATEGORIAS = [
        ('Matematicos', 'Matematicos'),
        ('Novidades', 'Novidades'),  
        ('Historia', 'Historia'),
        ('Exercicios', 'Exercicios'),   
    ]

    titulo = models.CharField(max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH,)  
    Texto = models.TextField(null=True, blank=True)
    imagem = models.ImageField(upload_to='imagens', null=True, blank=True)
    Resumo = models.CharField(max_length=255, null=True, blank=True)
    conteudo = models.CharField(max_length=100, null=True, blank=True)
    tipo_arquivo = models.CharField(max_length=50, null=True, blank=True)
    Url = models.CharField(max_length=100, null=True, blank=True)
    categoria_postagem = models.CharField(max_length=50, choices=CATEGORIAS)

    def __str__(self):
        return self.categoria_postagem


    
class MensagemContato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()

    def __str__(self):
        return self.nome
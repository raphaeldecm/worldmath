from django.forms import ModelForm
from django import forms
from .models import *
from core.widgets import GovbrSelect

class MatematicosForm(forms.ModelForm):

    imagem = forms.FileField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Imagem",
        })
    )
    Resumo = forms.CharField(
        widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Resumo",
    })
    )

    class Meta:
        model = Matematicos
        fields = '__all__'

class HistoriaForm(forms.ModelForm):

    imagem = forms.FileField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Imagem",
        })
    )

    class Meta:
        models = Historia
        fields = '__all__'

class ExerciciosForm(forms.ModelForm):
    Conteudo = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Conteudo",
        })
    )
    Formato = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Formato",
        })
    )
    Download = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Download",
        })
    )

    class Meta:
        model = Exercicios
        fields = '__all__'

class DiversidadesForm(forms.ModelForm):
    imagem = forms.FileField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Imagem",
        })
    )
    categoria_diversidades = forms.ChoiceField(
        choices=Diversidades.CategoriaDiversidades.choices,
        label="Categoria_Diversidades",
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Categoria_diversidade",
        })
    )

    class Meta:
        model = Diversidades
        fields = '__all__'
class PostagemForm(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = '__all__'

    Titulo = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Titulo",
        })
    )

    Texto = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Texto",
        })
    )

    categoria_postagem = forms.ChoiceField(
        choices=Postagem.CategoriaPostagem.choices,
        label="Categoria_Postagem",
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Categoria Postagem",
        })
    )

    Data_postagem = forms.DateField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Data_Postagem",
        })
    )
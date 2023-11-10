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
    Resumo = forms.TextInput(
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

    Conteudo = forms.TextInput(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Conteudo",
        })
    )
    Formato = forms.TextInput(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Formato",
        })
    )
    Download = forms.TextInput(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Download",
        })
    )
        
    class Meta:
        model = Historia
        fields = '__all__'

class DiversidadesForm(forms.ModelForm):

    imagem = forms.FileField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Imagem",
        })
    )
    categoria_diversidades = forms.ChoiceField(
        choices=Diversidades.categoria_diversidades.choices,
        label="Cetagoria_Diversidades",
        widget=GovbrSelect,
    )

    class Meta:
        models: Diversidades
        fiels = '__all__'

class PostagemForm(forms.FormModel):

    Titulo = forms.TextInput(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Titulo",
        })
    )

    Texto = forms.TextInput(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Texto",
        })
    )

    categoria_diversidades = forms.ChoiceField(
        choices=Postagem.categoria_postagem.choices,
        label="Cetagoria_Postagem",
        widget=GovbrSelect,
    )



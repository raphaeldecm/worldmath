from django import forms
from .models import Postagem

class PostagemForm(forms.ModelForm):
    CATEGORIAS = [
        ('Matematicos', 'Matematicos'),
        ('Novidades', 'Novidades'),  # Diversidades
        ('Historia', 'Historia'),
        ('Exercicios', 'Exercicios'),
    ]

    # categoria_postagem = forms.ChoiceField(
    #     choices=CATEGORIAS,
    #     label="Categoria da Postagem",
    #     widget=forms.Select(attrs={
    #         "class": "form-control",
    #         "placeholder": "Categoria da Postagem",
    #         "id": "id_categoria_postagem",  # Adicione um ID para referência no JavaScript
    #     })
    # )

    # titulo = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Titulo da postagem",
    #     })
    # )
    # Texto = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Texto da postagem",
    #     })
    # )
    # Imagem = forms.FileField(
    #     widget=forms.FileInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Imagem",
    #     })
    # )

    # Resumo = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Resumo da postagem",
    #     })
    # )
    # conteudo = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "conteudo da postagem",
    #     })
    # )
    # tipo_arquivo = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Tipo do arquivo",
    #     })
    # )
    # Url = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Url",
    #     })
    # )

    class Meta:
        model = Postagem
        fields = ['titulo', 'Texto', 'imagem', 'Resumo', 'conteudo', 'tipo_arquivo', 'Url', 'categoria_postagem']

    def __init__(self, *args, **kwargs):
        super(PostagemForm, self).__init__(*args, **kwargs)
        categoria = self.initial.get('categoria_postagem', None)
        self.adjust_fields_visibility(categoria)

    def adjust_fields_visibility(self, categoria):
        if 'Url' in self.fields:
            if categoria == 'Historia' or categoria == 'Matematicos':
                if 'Url' in self.fields:
                    self.fields['Url'].widget.attrs.pop('disabled', None)
                self.fields['conteudo'].widget.attrs.pop('disabled', None)
                self.fields['tipo_arquivo'].widget.attrs.pop('disabled', None)
            elif categoria == 'Exercicios':
                self.fields['imagem'].widget.attrs.pop('disabled', None)
                self.fields['Resumo'].widget.attrs.pop('disabled', None)
                self.fields['conteudo'].widget.attrs.pop('required', None)
                self.fields['tipo_arquivo'].widget.attrs.pop('required', None)
                self.fields['Url'].widget.attrs.pop('required', None)
            elif categoria == 'Novidades':
                self.fields['conteudo'].widget.attrs.pop('disabled', None)
                self.fields['tipo_arquivo'].widget.attrs.pop('disabled', None)
                self.fields['Url'].widget.attrs.pop('disabled', None)
                self.fields['imagem'].widget.attrs.pop('required', None)
                self.fields['Resumo'].widget.attrs.pop('required', None)



    # def clean(self):
    #     cleaned_data = super().clean()
    #     categoria = cleaned_data.get('categoria_postagem')

    #     if categoria == 'Historia' or categoria == 'Matematicos':
    #         cleaned_data['conteudo'] = ''
    #         cleaned_data['tipo_arquivo'] = ''
    #         if 'Url' in self.fields:
    #             self.fields['Url'].widget.attrs['disabled'] = True
    #     elif categoria == 'Exercicios':
    #         cleaned_data['imagem'] = None
    #         cleaned_data['Resumo'] = ''
    #     elif categoria == 'Diversidades':
    #         cleaned_data['conteudo'] = ''
    #         cleaned_data['tipo_arquivo'] = ''
    #         cleaned_data['Url'] = ''

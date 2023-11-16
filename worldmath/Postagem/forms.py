from django import forms
from .models import Postagem

class PostagemForm(forms.ModelForm):
    CATEGORIAS = [
        ('Matematicos', 'Matematicos'),
        ('Novidades', 'Novidades'),  # Diversidades
        ('Historia', 'Historia'),
        ('Exercicios', 'Exercicios'),
    ]

    categoria_postagem = forms.ChoiceField(
        choices=CATEGORIAS,
        label="Categoria da Postagem",
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Categoria da Postagem",
            "id": "id_categoria_postagem",  # Adicione um ID para referência no JavaScript
        })
    )

    class Meta:
        model = Postagem
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Título da postagem",
            }),
            'Data_postagem': forms.DateInput(attrs={
                "class": "form-control",
                "placeholder": "Data da Postagem",
                "type": "date",  # Adiciona o tipo de input para data
            }),
            'Texto': forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Texto",
            }),
            'imagem': forms.FileInput(attrs={
                "class": "form-control",
                "placeholder": "Imagem",
            }),
            'Resumo': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Resumo",
            }),
            'conteudo': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Conteúdo",
            }),
            'tipo_arquivo': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Tipo do Arquivo",
            }),
            'Url': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "URL",
            }),
            'categoria_diversidades': forms.Select(attrs={
                "class": "form-control",
                "placeholder": "Categoria Diversidades",
            }),
        }

    def __init__(self, *args, **kwargs):
        super(PostagemForm, self).__init__(*args, **kwargs)
        categoria = self.initial.get('categoria_postagem', None)
        self.adjust_fields_visibility(categoria)

    def adjust_fields_visibility(self, categoria):
        if categoria == 'Historia' or categoria == 'Matematicos':
            self.fields['conteudo'].widget.attrs.pop('disabled', None)
            self.fields['tipo_arquivo'].widget.attrs.pop('disabled', None)
            self.fields['url'].widget.attrs.pop('disabled', None)
        elif categoria == 'Exercicios':
            self.fields['imagem'].widget.attrs.pop('disabled', None)
            self.fields['resumo'].widget.attrs.pop('disabled', None)
            self.fields['conteudo'].widget.attrs.pop('required', None)
            self.fields['tipo_arquivo'].widget.attrs.pop('required', None)
            self.fields['url'].widget.attrs.pop('required', None)
        elif categoria == 'Diversidades':
            self.fields['conteudo'].widget.attrs.pop('disabled', None)
            self.fields['tipo_arquivo'].widget.attrs.pop('disabled', None)
            self.fields['url'].widget.attrs.pop('disabled', None)
            self.fields['imagem'].widget.attrs.pop('required', None)
            self.fields['resumo'].widget.attrs.pop('required', None)

    def clean(self):
        cleaned_data = super().clean()
        categoria = cleaned_data.get('categoria_postagem')

        if categoria == 'Historia' or categoria == 'Matematicos':
            cleaned_data['conteudo'] = ''
            cleaned_data['tipo_arquivo'] = ''
            cleaned_data['url'] = ''
        elif categoria == 'Exercicios':
            cleaned_data['imagem'] = None
            cleaned_data['resumo'] = ''
        elif categoria == 'Diversidades':
            cleaned_data['conteudo'] = ''
            cleaned_data['tipo_arquivo'] = ''
            cleaned_data['url'] = ''

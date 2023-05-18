from django import forms

class FaleConoscoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get('nome')
        email = cleaned_data.get('email')
        mensagem = cleaned_data.get('mensagem')
        if not nome:
            raise forms.ValidationError('Por favor, digite seu nome.')
        if not email:
            raise forms.ValidationError('Por favor, digite seu email.')
        if not mensagem:
            raise forms.ValidationError('Por favor, digite sua mensagem.')


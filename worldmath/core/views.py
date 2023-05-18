from django.shortcuts import render
from .forms import FaleConoscoForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def arquimedes(request):
    return render(request, 'arquimedes.html')

def descartes(request):
    return render(request, 'descartes.html')

def euclides(request):
    return render(request, 'euclides.html')

def euler(request):
    return render(request, 'euler.html')

def pitagoras(request):
    return render(request, 'pitagoras.html')

def exercicios(request):
    return render(request, 'exercicios.html')

def matematica(request):
    return render(request, 'matematica.html')

def Poesias(request):
    return render(request, 'Poesias.html')

def Poesias2(request):
    return render(request, 'Poesias2.html')

def faleconosco(request):
    if request.method == 'POST':
        form = FaleConoscoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            print(f'Nome: {nome}')
            print(f'Email: {email}')
            print(f'Mensagem: {mensagem}')
    else:
        form = FaleConoscoForm()
    return render(request, 'faleconosco.html', {'form': form})



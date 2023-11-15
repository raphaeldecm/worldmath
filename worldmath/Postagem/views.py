from django.shortcuts import render
from django.views import generic
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def Login(request):
    return render(request, 'Login.html')

class IndexView(generic.TemplateView):
    template_name = "index.html"

class ArquimedesView(generic.TemplateView):
    template_name = "arquimedes.html"
    
class ExerciciosView(generic.TemplateView):
    template_name = "exercicios.html"

class MatematicaView(generic.TemplateView):
    template_name = "matematica.html"

class PostagemCreateView(views.SuccessMessageMixin, generic.CreateView):
    model = Postagem
    form_class = PostagemForm
    template_name = "dashboard/Postagem_form.html"
    success_message = "Postagem cadastrada com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['matematicos_form'] = MatematicosForm()
        context['historia_form'] = HistoriaForm()
        context['exercicios_form'] = ExerciciosForm()
        context['diversidades_form'] = DiversidadesForm()
        return context

class PostagemListView(LoginRequiredMixin, generic.ListView):
    model = Postagem
    paginate_by = 5
    template_name = "dashboard/Postagem_List.html"
    
    def get_queryset(self):
        return Postagem.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_postagem'] = Postagem.objects.count()
        return context

def get_category_fields(request, category):
    if category == 'Matematicos':
        form = MatematicosForm()
    elif category == 'Historia':
        form = HistoriaForm()
    elif category == 'Exercicios':
        form = ExerciciosForm()
    elif category == 'Diversidades':
        form = DiversidadesForm()
    else:
        return JsonResponse({'error': 'Categoria inválida'})

    context = {'form': form}
    return render(request, 'dashboard/categoria_fields.html', context)

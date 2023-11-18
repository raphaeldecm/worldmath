from django.shortcuts import render
from django.views import generic
from django.contrib.messages import views
from django.urls import reverse_lazy
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
    success_url = reverse_lazy("Postagem:Lista_postagem")
    
    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        print("Deu bom")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione o seguinte contexto para garantir que o campo correto seja exibido
        context['form'] = PostagemForm(initial={'categoria_postagem': self.request.POST.get('categoria_postagem')})
        return context

class PostagemListView(LoginRequiredMixin, generic.ListView):
    model = Postagem
    template_name = "dashboard/Postagem_List.html"
    
    def get_queryset(self):
        return Postagem.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_postagem'] = Postagem.objects.count()
        return context

class PostagemDeleteView(LoginRequiredMixin, views.SuccessMessageMixin, generic.DeleteView):
    model = Postagem
    success_url = reverse_lazy("Postagem:Lista_postagem")
    success_message = "Reserva deletada com sucesso"

class PostagemDetailView(LoginRequiredMixin, generic.DetailView):
    model = Postagem

class PostagemUpdateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = Postagem
    form_class = PostagemForm
    success_url = reverse_lazy("Postagem:Lista_postagem")
    template_name = "dashboard/Postagem_form.html"
    success_message = "Reserva atualizada com sucesso"
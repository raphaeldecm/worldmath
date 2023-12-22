from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from django.views import generic
from django.contrib.messages import views
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from users.permissions import RedatorPermission, AdministradorPermission
from django_filters.views import FilterView


# Create your views here.

def Login(request):
    return render(request, 'Login.html')

class IndexView(generic.ListView):
    model = Postagem
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtenha o objeto mais recente da categoria 'Matematicos'
        first_object_matematicos = Postagem.objects.filter(categoria_postagem='Matematicos').order_by('-created_at').first()
        context['first_object_matematicos'] = first_object_matematicos
        
        latest_objects_novidades = Postagem.objects.filter(categoria_postagem='Novidades').order_by('-created_at')[:3]
        context['latest_objects_novidades'] = latest_objects_novidades

        return context

class GalleryView(generic.ListView):    
    model = Postagem
    template_name = "gallery.html"

class MatematicosDetailView(generic.DetailView):
    model = Postagem
    template_name = "Math_detail.html"

class NovidadesDetailView(generic.DetailView):
    model = Postagem
    template_name = "Novidades_detalhe.html"
    
class ExerciciosView(generic.ListView):
    model = Postagem
    template_name = "exercicios.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        conteudo = self.request.GET.get('conteudo')
    
        if conteudo:
            queryset = queryset.filter(titulo__icontains=conteudo)

        return queryset 

class HistoriaView(generic.ListView):
    model = Postagem
    template_name = "historia.html"

class NovidadesView(generic.ListView):
    model = Postagem
    template_name = "Novidades.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtenha o objeto mais recente da categoria 'Matematicos'
        first_object = Postagem.objects.filter(categoria_postagem='Novidades').order_by('-created_at').first()
            
        context['first_object'] = first_object
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        titulo = self.request.GET.get('titulo')
        conteudo = self.request.GET.get('conteudo')
        Resumo = self.request.GET.get('Resumo')

        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)

        if conteudo:
            queryset = queryset.filter(conteudo__icontains=conteudo)

        if Resumo:
            queryset = queryset.filter(Resumo__icontains=conteudo)

        return queryset
        
class ResultadoNovidadesView(generic.ListView):
    model = Postagem
    template_name = 'Resultado_Novidades.html'
    context_object_name = 'resultados'

    def get_queryset(self):
        queryset = Postagem.objects.filter(categoria_postagem='Novidades')
        titulo = self.request.GET.get('titulo')
        conteudo = self.request.GET.get('conteudo')
        Resumo = self.request.GET.get('Resumo')

        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)

        if conteudo:
            queryset = queryset.filter(conteudo__icontains=conteudo)

        if Resumo:
            queryset = queryset.filter(Resumo__icontains=Resumo)

        return queryset

class PostagemCreateView(RedatorPermission, LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
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

class PostagemListView(RedatorPermission, LoginRequiredMixin, generic.ListView):
    model = Postagem
    paginate_by = 5
    template_name = "dashboard/Postagem_List.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_postagem'] = Postagem.objects.count()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        titulo = self.request.GET.get('titulo')
        categoria_postagem = self.request.GET.get('categoria_postagem')

        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)

        if categoria_postagem:
            queryset = queryset.filter(categoria_postagem__icontains=categoria_postagem)

        return queryset.filter(created_by=self.request.user)


class PostagemDeleteView(RedatorPermission, LoginRequiredMixin, views.SuccessMessageMixin, generic.DeleteView):
    model = Postagem
    success_url = reverse_lazy("Postagem:Lista_postagem")
    success_message = "Reserva deletada com sucesso"

class PostagemDetailView(RedatorPermission, LoginRequiredMixin, generic.DetailView):
    model = Postagem
    template_name = "dashboard/Postagem_detail.html"

class PostagemUpdateView(RedatorPermission, LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = Postagem
    form_class = PostagemForm
    success_url = reverse_lazy("Postagem:Lista_postagem")
    template_name = "dashboard/Postagem_form.html"
    success_message = "Reserva atualizada com sucesso"

    
class ContatoView(views.SuccessMessageMixin, FormView):
    template_name = 'FormContact.html'
    form_class = FormularioContato
    success_url = reverse_lazy('Postagem:contato')
    success_message = "Mensagem enviada com sucesso!"

    def form_valid(self, form):
        # Salvando o formulário
        mensagem_contato = form.save(commit=False)

        # Obtendo o endereço de e-mail do usuário que está enviando a mensagem
        remetente = form.cleaned_data['email']

        # Salvando o restante do formulário e enviando o e-mail
        mensagem_contato.save()

        assunto = 'Nova mensagem de contato'
        mensagem = f'Nome: {mensagem_contato.nome}\nE-mail: {mensagem_contato.email}\nMensagem: {mensagem_contato.mensagem}'
        destinatario = ['worldmath34@gmail.com']

        send_mail(assunto, mensagem, remetente, destinatario, fail_silently=False)

        return super().form_valid(form)
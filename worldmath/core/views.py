from django.shortcuts import render
from django.views import generic
from worldmath.Postagem.models import *
from worldmath.users.models import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_postagem'] = Postagem.objects.count()
        context['num_usuarios'] = User.objects.count()
        return context


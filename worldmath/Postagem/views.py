from django.shortcuts import render
from django.views import generic
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"

class ArquimedesView(generic.TemplateView):
    template_name = "arquimedes.html"
    
class ExerciciosView(generic.TemplateView):
    template_name = "exercicios.html"

class MatematicaView(generic.TemplateView):
    template_name = "matematica.html"

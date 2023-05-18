from django.urls import path

from .views import index, arquimedes, descartes, euclides, euler, exercicios, matematica, pitagoras, Poesias, Poesias2, faleconosco

urlpatterns = [
    path('', index, name='index'),
    path('arquimedes', arquimedes, name='arquimedes'),
    path('descartes', descartes, name='descartes'),
    path('euclides', euclides, name='euclides'),
    path('euler', euler, name='euler'),
    path('exercicios', exercicios, name='exercicios'),
    path('matematica', matematica, name='matematica'),
    path('pitagoras', pitagoras, name='pitagoras'),
    path('Poesias', Poesias, name='Poesias'),
    path('Poesias2', Poesias2, name='Poesias2'),
    path('faleconosco', faleconosco, name='faleconosco'),
]

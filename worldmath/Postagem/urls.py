from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name = "Postagem"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('arquimedes', views.ArquimedesView.as_view(), name='arquimedes'),
    path('exercicios', views.ExerciciosView.as_view(), name='exercicios'),
    path('matematica', views.MatematicaView.as_view(), name='matematica'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


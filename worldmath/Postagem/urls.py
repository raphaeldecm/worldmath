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
    path('Cadastrar_postagem/', views.PostagemCreateView.as_view(), name='CadastroPostagem'),
    path('Lista_postagem/', views.PostagemListView.as_view(), name='Lista_postagem'),
    path('Delete_postagem/<int:pk>/', views.PostagemDeleteView.as_view(), name='Delete_postagem'),
    path('Update_postagem/<int:pk>/', views.PostagemUpdateView.as_view(), name='Editar_postagem'),
    path('Detalhe_postagem/<int:pk>/', views.PostagemDetailView.as_view(), name='Detail_postagem'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


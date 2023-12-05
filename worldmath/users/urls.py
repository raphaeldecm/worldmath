from django.urls import path

from worldmath.users.views import *
from . import views

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path('list_users/', views.UsersListView.as_view(), name='lista_usuarios'),
    path('create_users/', views.UserCreateView.as_view(), name='create_users'),
    path('<str:username>/', view=user_detail_view, name='detail'),
    path('delete_users/<int:pk>/', views.UserDeleteView.as_view(), name='delete_users'),
    path("edit/<int:pk>/", view=ThirdUserUpdateView.as_view(), name="edit"),
    path('atualizar-grupo-administrador/<int:pk>/', views.AtualizarGrupoAdministradorView.as_view(), name='atualizar_grupo_administrador'),
    path('remover-grupo-administrador/<int:pk>/', views.RemoveGrupoAdministradorView.as_view(), name='remover_grupo_administrador'),
]

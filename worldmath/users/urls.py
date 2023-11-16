from django.urls import path

from worldmath.users.views import *
from . import views
app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path('list_users', views.UsersListView.as_view(), name='lista_usuarios'),
    path('delete_users/<int:pk>/', views.UserDeleteView.as_view(), name='delete_users'),
]

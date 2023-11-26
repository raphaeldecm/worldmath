from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *   
from . import views     

app_name = "core"
urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
#    path('', views.HomeView.as_view(), name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


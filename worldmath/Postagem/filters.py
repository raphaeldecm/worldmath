import django_filters

from .models import Postagem


class PostagemFilter(django_filters.FilterSet):
    categoria_postagem = django_filters.CharFilter(lookup_expr='icontains', label='Sua Label Categoria')
    titulo = django_filters.CharFilter(lookup_expr='icontains', label='Sua Label Título')

    class Meta:
        model = Postagem
        fields = ['categoria_postagem', 'titulo']
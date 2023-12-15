from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.messages import views
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, DeleteView, CreateView
from django.views import generic
from django.contrib.auth.models import Group, Permission
from users.permissions import RedatorPermission, AdministradorPermission
from django.views import View
from django.shortcuts import get_object_or_404
from .forms import UserAdminCreationForm, UserSignupForm

User = get_user_model()


class HomeView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = "base_dashboard.html"
    

class UserDetailView(AdministradorPermission,LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(AdministradorPermission,LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"] 
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()

class UserRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()

class UsersListView(AdministradorPermission, LoginRequiredMixin, generic.ListView):
    model = User
    paginate_by = 5
    ordering = ["name"]
    template_name = "lista_users.html"

    def get_queryset(self):
        return User.objects.exclude(username='').order_by('name')    


class UserDeleteView(AdministradorPermission, LoginRequiredMixin, generic.DeleteView):
    model = User
    success_url = reverse_lazy("users:lista_usuarios")
    success_message = "reserva cancelada com sucesso!!"


class RemoveGrupoAdministradorView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs['pk'])
        grupo_administrador = Group.objects.get(name='Redator')

        # Remove o usuário do grupo "Administrador"
        user.groups.remove(grupo_administrador)

        return HttpResponseRedirect(reverse('users:lista_usuarios'))
class AtualizarGrupoAdministradorView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs['pk'])
        grupo_administrador = Group.objects.get(name='Redator')

        # Adiciona o usuário ao grupo "Administrador"
        user.groups.add(grupo_administrador)

        return HttpResponseRedirect(reverse('users:lista_usuarios'))


class ThirdUserUpdateView(LoginRequiredMixin, views.SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserAdminCreationForm
    success_url = reverse_lazy("users:list")
    success_message = _("Usuário atualizado com sucesso!")
    template_name = "account/signup.html"



class UserCreateView(LoginRequiredMixin, views.SuccessMessageMixin, CreateView):
    model = User
    form_class = UserSignupForm
    success_url = reverse_lazy("users:list")
    success_message = _("Usuário cadastrado com sucesso! Se quiser ser um Redator, entre em contato conosco.")
    template_name = "account/signup.html"

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, DeleteView
from django.views import generic
from users.permissions import AdministradorPermission, SuperAdministradorPermission

User = get_user_model()


class UserDetailView(SuperAdministradorPermission,LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(SuperAdministradorPermission,LoginRequiredMixin, SuccessMessageMixin, UpdateView):
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

class UsersListView(SuperAdministradorPermission, LoginRequiredMixin, generic.ListView):
    model = User
    paginate_by = 5
    ordering = ["name"]
    template_name = "lista_users.html"

class UserDeleteView(SuperAdministradorPermission, LoginRequiredMixin, generic.DeleteView):
    model = User
    success_url = reverse_lazy("users:lista_usuarios")
    success_message = "reserva cancelada com sucesso!!"
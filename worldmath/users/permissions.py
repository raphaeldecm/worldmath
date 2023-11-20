from django.contrib.auth.mixins import UserPassesTestMixin


class AdministradorPermission(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name="Administrador").exists():
            return True
        return False

class SuperAdministradorPermission(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name="SuperAdministrador").exists():
            return True
        return False
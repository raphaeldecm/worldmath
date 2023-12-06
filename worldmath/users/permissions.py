from django.contrib.auth.mixins import UserPassesTestMixin


class RedatorPermission(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name="Redator").exists():
            return True
        return False

class AdministradorPermission(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name="Administrador").exists():
            return True
        return False
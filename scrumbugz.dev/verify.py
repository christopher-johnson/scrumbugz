# verify.py
from django_browserid.views import Verify
class Verifyclass(Verify):
    @property
    def success_url(self):
        if self.user.username == 'Admin':
            return '/admin'
        # the default behaviour
        return getattr(settings, 'LOGIN_REDIRECT_URL', '/')

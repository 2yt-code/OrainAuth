from django.shortcuts import redirect
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from accounts.decorators import redirect_if_authenticated

# Since the Send Reset Password in Email system is for Django itself,
# that is, it is the default, we have to make it work in our Django custom classes so that if the user is logged into their account,
# they will go to the dashboard page
class RedirectDashboard:
    @redirect_if_authenticated('dashboard')
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# -------------------
# Redirect operation
# -------------------
class CustomPasswordResetView(RedirectDashboard, PasswordResetView):
    pass
class CustomPasswordResetDoneView(RedirectDashboard, PasswordResetDoneView):
    pass
class CustomPasswordResetConfirmView(RedirectDashboard, PasswordResetConfirmView):
    pass
class CustomPasswordResetCompleteView(RedirectDashboard, PasswordResetCompleteView):
    pass

from django.shortcuts import redirect
from django.contrib.auth import logout

from accounts.decorators import redirect_if_not_authenticated

# ---------------
# Logout Section
# ---------------
@redirect_if_not_authenticated(path='login')
def logout_accounts(request):
    # The session is cleared from both the database and the user’s browser
    logout(request)
    return redirect('login')
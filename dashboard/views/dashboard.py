from django.shortcuts import render
from accounts.decorators import redirect_if_not_authenticated

# ------------------------
# Dashboard Index Section
# ------------------------
@redirect_if_not_authenticated(path='login')
def dashboard_page(request):
    # User information
    user = request.user

    # users/dashboard.html template
    return render(request, template_name='users/dashboard.html', context={'user': user})
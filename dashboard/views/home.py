from django.shortcuts import render
from accounts.decorators import redirect_if_not_authenticated

#  -------------
# Home Section
# -------------
@redirect_if_not_authenticated(path='login')
def home_page(request):
    # User information
    user = request.user

    # users/home.html template
    return render(request, template_name='users/home.html', context={'user': user})
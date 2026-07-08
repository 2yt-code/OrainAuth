from django.shortcuts import render

from accounts.decorators import redirect_if_not_authenticated

# ----------------
# Profile Section
# ----------------
@redirect_if_not_authenticated(path='login')
def profile_page(request):
    # User information
    user = request.user
    
    # users/profile.html template
    return render(request, template_name='users/profile.html', context={'user': user})

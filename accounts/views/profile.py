from django.shortcuts import render

from accounts.decorators import redirect_if_not_authenticated


@redirect_if_not_authenticated(path='login')
def profile_page(request):
    return render(request, template_name='users/profile.html', context={'user': request.user})

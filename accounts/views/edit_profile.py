from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.decorators import redirect_if_not_authenticated
from accounts.forms import UserUpdateForm


@redirect_if_not_authenticated(path='login')
def edit_profile(request):
    if request.method == "POST":
        post_data = request.POST.copy()
        form = UserUpdateForm(post_data, instance=request.user)
            
        if form.is_valid():
            form.save()

            return redirect('profile')

        else:
            messages.error(request, 'Error: Please try again')
            
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, template_name='users/edit_profile.html', context={'form': form})
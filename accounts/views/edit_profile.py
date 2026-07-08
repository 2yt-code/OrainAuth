from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.decorators import redirect_if_not_authenticated
from accounts.forms import UserUpdateForm

# ---------------------
# Edit Profile Section
# ---------------------
@redirect_if_not_authenticated(path='login')
def edit_profile(request):
    if request.method == "POST":
        # Receive information entered by the user
        post_data = request.POST.copy()
        # Change in database
        form = UserUpdateForm(post_data, instance=request.user)
            
        if form.is_valid():
            # Save in database
            form.save()

            return redirect('profile')

        else:
            messages.error(request, 'Error: Please try again')
            
    else:
        # Initial template for GET method
        form = UserUpdateForm(instance=request.user)

    # users/edit_profile.html template
    return render(request, template_name='users/edit_profile.html', context={'form': form})
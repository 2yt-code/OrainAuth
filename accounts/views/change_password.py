from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from accounts.decorators import redirect_if_not_authenticated
from accounts.forms import PasswordUpdateForm

# ----------------------
# Edit Password Section
# ----------------------
@redirect_if_not_authenticated(path='login')
def change_password(request):
    if request.method == "POST":
        # Comparison between new request and old information
        form = PasswordUpdateForm(request.POST)

        if form.is_valid():
            user = request.user
                
            old_pw = form.cleaned_data['old_password']
            new_pw = form.cleaned_data['new_password']

            if user.check_password(old_pw):
                if old_pw == new_pw:
                    # If the new password matches the old password
                    messages.error(request, 'New password must not match the old password')
                    return redirect('change_password')

                # Hashing new password
                user.set_password(new_pw)
                # Save in DB
                user.save()

                # Preventing user session changes in the database to avoid being logged out of the system
                update_session_auth_hash(request, user)
                return redirect('profile')
                
            else:
                # If current password does not match
                messages.error(request, 'Current password is incorrect')
                return redirect('change_password')

        else:
            # If everything wasn't okay
            messages.error(request, 'Password and Confirm Password Field do not match')

    else:
        # Initial template for GET method
        form = PasswordUpdateForm()

    # users/change_password.html template
    return render(request, template_name='users/change_password.html', context={'form': form})
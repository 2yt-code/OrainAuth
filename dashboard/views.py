from django.shortcuts import render, redirect

# ----------------------------------------
# System Authentication Section Templates
# ----------------------------------------
class Template:
    TEMPLATE_HOME = 'home.html'
    TEMPLATE_DASHBOARD = 'users/dashboard.html'

# -------------
# Home Section
# -------------
def home_page(request):
    if not request.user.is_authenticated:
        # If the user not logged in
        return render(request, template_name=Template.TEMPLATE_HOME)

    else:
        # User information
        user = request.user

        return render(request, template_name=Template.TEMPLATE_HOME, context={'user': user})


# ------------------------
# Dashboard Index Section
# ------------------------
def dashboard_index_page(request):
    if not request.user.is_authenticated:
        # If the user not logged in
        return redirect('login')
    
    else:
        # User information
        user = request.user

    return render(request, template_name=Template.TEMPLATE_DASHBOARD, context={'user': user})
# adminpanel/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import UserProfile

def admin_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            admin = form.save()
            login(request, admin)
            return redirect('admin_dashboard')  # ✅ make sure this name exists in urls.py
    else:
        form = UserCreationForm()
    return render(request, 'adminpanel/signup.html', {'form': form})


@login_required(login_url='admin_signin')
def admin_dashboard(request):
    users = UserProfile.objects.all()
    return render(request, 'adminpanel/dashboard.html', {'users': users})


def admin_signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('admin_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'adminpanel/signin.html', {'form': form})


@login_required
def admin_logout(request):
    logout(request)
    return redirect('admin_signin')

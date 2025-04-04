from django.shortcuts import render, redirect,HttpResponse
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms

def home(request):
    return render(request, 'users/index.html')

def event_view(request):
    return render(request, 'users/event.html')

def contact(request):
    return render(request, 'users/contact.html')

def user_profile(request):
    """
    Handles both displaying the profile form and showing preview after submission.
    """
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        bio = request.POST.get("bio")

        UserProfile.objects.create(name=name, email=email, phone=phone, bio=bio)
        return render(request, "users/profile.html", {
            "preview": True,
            "name": name,
            "email": email,
            "phone": phone,
            "bio": bio,
        })

    return render(request, "users/profile.html", {"preview": False})


def create_profile(request):
    """
    Optional: Used only if you want to use Django forms.
    """
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UserProfileForm()
    return render(request, 'users/create_profile.html', {'form': form})


def view_profile(request):
    """
    Display last created profile.
    """
    profile = UserProfile.objects.last()  # For demo/testing purposes
    return render(request, 'users/view_profile.html', {'profile': profile})

def register_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'users/dashboard.html')

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def show_users(request):
    users = User.objects.all()
    return render(request, 'show_users.html', {'users': users})

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Adjust if your profile view is named differently
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'users/update_profile.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
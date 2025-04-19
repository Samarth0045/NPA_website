from django.shortcuts import render, redirect,HttpResponse
from .forms import UserProfileForm,NotificationForm,LocationForm
from .models import UserProfile, Notification,District, Taluka
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

from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    """
    Handles both displaying the profile form and showing preview after submission.
    """
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        bio = request.POST.get("bio")
        age = request.POST.get("age")
        designation = request.POST.get("designation")

        # ✅ Save all fields including age and designation
        UserProfile.objects.create(
            user=request.user,
            name=name,
            email=email,
            phone=phone,
            bio=bio,
            age=age,
            designation=designation
        )

        return render(request, "users/profile.html", {
            "preview": True,
            "name": name,
            "email": email,
            "phone": phone,
            "bio": bio,
            "age": age,
            "designation": designation,
        })

    return render(request, "users/profile.html", {"preview": False})


def edit_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to a profile detail page
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'user/update_profile.html', {'form': form})

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
        return redirect('user_dashboard')  # ✅ FIXED NAME

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_dashboard')  # ✅ FIXED NAME
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
            return redirect('user_dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required(login_url='login')
def dashboard(request):
    # Get the user profile for the logged-in user
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None  # If no profile exists, set it to None

    return render(request, 'users/dashboard.html', {
        'user_profile': user_profile,  # Pass the user profile to the template
    })


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

def notification_board(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notification_board')
    else:
        form = NotificationForm()
    notifications = Notification.objects.order_by('-created_at')
    return render(request, 'users/notification_board.html', {'form': form, 'notifications': notifications})

def location_selector(request):
    districts = District.objects.all()
    return render(request, 'users/location_selector.html', {'districts': districts})

def load_talukas(request):
    district_id = request.GET.get('district_id')
    talukas = Taluka.objects.filter(district_id=district_id).values('id', 'name')
    return JsonResponse(list(talukas), safe=True)

def send_whatsapp_message(to, message):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    from_whatsapp_number = 'whatsapp:+14155238886'  # Twilio sandbox number

    client = Client(account_sid, auth_token)

    client.messages.create(
        body=message,
        from_=from_whatsapp_number,
        to=f'whatsapp:{to}'
    )

def notify_community(request):
    users = User.objects.all()  # Or filter by district/taluka
    for user in users:
        send_whatsapp_message(user.phone, "📢 Meeting at 5 PM today in your Taluka office.")
    messages.success(request, "Notifications sent!")
    return redirect('home')
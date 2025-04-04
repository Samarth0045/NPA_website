from django.urls import path
from . import views
from .views import user_list

urlpatterns = [
    path('', views.home, name='home'),
    path('event/', views.event_view, name='event'),
    path('contact/', views.contact, name='contact'),

    # Profile-related paths
    path('profile/', views.user_profile, name='user_profile'),              # Combined view or form entry point
    path('profile/create/', views.create_profile, name='create_profile'),   # Profile form submission
    path('profile/view/', views.view_profile, name='view_profile'),         # Profile preview/display

    #user-authentication
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    #user-list check
    path('users/', views.user_list, name='user_list'),
    path('users/', views.show_users, name='user_list'),
    path('update/', views.update_profile, name='update_profile'),
    path('profile/', views.profile, name='profile'),
]

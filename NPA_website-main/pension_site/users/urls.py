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
    path('signup/', views.register_user, name='user_signup'),
    path('signin/', views.login_user, name='user_login'),
    path('dashboard/', views.dashboard, name='user_dashboard'),
    path('logout/', views.logout_user, name='user_logout'),

    #user-list check
    path('users/', views.user_list, name='user_list'),
    path('users/', views.show_users, name='user_list'),
    path('update/', views.update_profile, name='update_profile'),
    path('profile/', views.profile, name='profile'),

    #notification
    path('notifications/', views.notification_board, name='notification_board'),

    #district-talukar-city/village
    path('location/', views.location_selector, name='location_selector'),
    path('ajax/load-talukas/', views.load_talukas, name='ajax_load_talukas'),
]

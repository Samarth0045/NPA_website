from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.admin_signup, name='admin_signup'),
    path('signin/', views.admin_signin, name='admin_signin'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.admin_logout, name='admin_logout'),
]

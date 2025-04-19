from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', include('users.urls')), 
    path('users/', include('users.urls')), # This will handle the homepage route
    path('admin/', admin.site.urls),
    path('adminpanel/', include('adminpanel.urls')),

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
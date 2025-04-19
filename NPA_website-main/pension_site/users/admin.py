from django.contrib import admin
from .models import District, Taluka,UserLocation

# Register your models here.
admin.site.register(District)
admin.site.register(Taluka)
admin.site.register(UserLocation)
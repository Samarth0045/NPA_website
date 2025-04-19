from django.contrib import admin
from .models import AdminUser, RegularUser

# Register your models here.
admin.site.register(AdminUser)
admin.site.register(RegularUser)
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=Truesz)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    bio = models.TextField(blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    designation = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name or "Unnamed Profile"

class Notification(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.message[:50]} - {self.created_at}"

class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Taluka(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='talukas')

    def __str__(self):
        return self.name
    
class UserLocation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Assuming you are using the default User model
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    taluka = models.ForeignKey(Taluka, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.district.name}, {self.taluka.name},'
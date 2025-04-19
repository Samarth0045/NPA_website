from django.db import models

class AdminUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)  # Store hashed in production!

    def __str__(self):
        return self.username


class RegularUser(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

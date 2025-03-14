from django.db import models
from django.conf import settings

class Driver(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='driver_profile')
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  license_number = models.CharField(max_length=50, unique=True)
  phone_number = models.CharField(max_length=15)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f"{self.first_name} {self.last_name}"
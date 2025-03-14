from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


VEHICLE_TYPES = [
    ('towncar', 'Towncar'),
    ('suv', 'SUV'),
    ('van', 'Van'),
    ('limo', 'Limousine'),
]

RELIABILITY_CHOICES = [
    ('excellent', 'Excellent'),
    ('good', 'Good'),
    ('average', 'Average'),
    ('poor', 'Poor'),
]


PASSENGER_LIMIT_CHOICES = [
    (1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),
]

class User(AbstractUser):
    is_active = models.BooleanField(default=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    street_address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    preferred_contact_method = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
  
class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPES)
    reliability = models.CharField(max_length=10, choices=RELIABILITY_CHOICES)
    passenger_limit = models.IntegerField(choices=PASSENGER_LIMIT_CHOICES, default=4)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)
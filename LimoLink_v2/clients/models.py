from django.db import models
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

STATUS = [
    ('scheduled', 'Scheduled'),
    ('completed', 'Completed'),
    ('canceled', 'Canceled'),
]

PASSENGER_LIMIT_CHOICES = [
    (1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),
]

class User(AbstractUser):
    pass

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
    
class Booking(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True, related_name='updated_bookings')
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    airline = models.CharField(max_length=100, blank=True)
    passengers = models.IntegerField()
    pickup_time = models.DateTimeField()
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=[('cash', 'Cash'), ('card', 'Credit/Debit Card')])
    status = models.CharField(max_length=10, choices=STATUS, default='scheduled')
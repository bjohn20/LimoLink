from django.db import models
from django.conf import settings
from drivers.models import Driver

STATUS_CHOICES = [
    ('scheduled', 'Scheduled'),
    ('completed', 'Completed'),
    ('canceled', 'Canceled'),
]

PAYMENT_METHOD_CHOICES = [
    ('cash', 'Cash'),
    ('credit_card', 'Credit Card'),
]

AIRLINE_CHOICES = [
    ("Delta", "Delta Airlines"),
    ("United", "United Airlines"),
    ("American", "American Airlines"),
    ("Southwest", "Southwest Airlines"),
    ("Spirit", "Spirit Airlines"),
    ("Frontier", "Frontier Airlines"),
    ("Frontier", "Frontier Airlines"),
    ("N/A", "N/A"),
]

class Booking(models.Model):
  
  # Relationships
  client = models.ForeignKey('clients.Client', on_delete=models.CASCADE, related_name='bookings')
  driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
  created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='updated_bookings')
  
  # Pickup Location
  pickup_street_address = models.CharField(max_length=255)
  pickup_city = models.CharField(max_length=100, blank=True, null=True) 
  pickup_state = models.CharField(max_length=2, blank=True, null=True)
  pickup_zip_code = models.CharField(max_length=10, blank=True, null=True)
  
  # Dropoff Location
  dropoff_street_address = models.CharField(max_length=255)
  dropoff_city = models.CharField(max_length=100,  blank=True, null=True)
  dropoff_state = models.CharField(max_length=2, blank=True, null=True)
  dropoff_zip_code = models.CharField(max_length=10, blank=True, null=True)
  
  # Flight Information 
  airline = models.CharField(max_length=50, choices=AIRLINE_CHOICES)
  other_airline = models.CharField(max_length=100, blank=True, null=True)
  flight_number = models.CharField(max_length=10, blank=True, null=True)
  
  # Passenger Information 
  passengers = models.IntegerField()
  pickup_time = models.DateTimeField()
  
  # Fare & Payment Information
  fare = models.DecimalField(max_digits=10, decimal_places=2)
  payment_method = models.CharField(max_length=11, choices=PAYMENT_METHOD_CHOICES)
  
  # Status
  status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled') 
  
  def __str__(self):
    return f"Booking #{self.id} - {self.client} ({self.status})"
# Compare this snippet from LimoLink_v2/clients/views.py: 

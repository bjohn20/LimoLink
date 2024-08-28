from django.db import models

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


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)


class Driver(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPES)
    reliability = models.CharField(max_length=10, choices=RELIABILITY_CHOICES)
    passenger_limit = models.IntegerField()

class Trip(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    airline = models.CharField(max_length=100, blank=True)
    passengers = models.IntegerField()
    pickup_time = models.DateTimeField()
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=[('cash', 'Cash'), ('card', 'Credit/Debit Card')])
    status = models.CharField(max_length=10, choices=STATUS, default='scheduled')


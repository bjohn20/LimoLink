from django import forms
from .models import Customer, Trip, Driver

class CustomerForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ['first_name', 'last_name', 'email', 'phone']

class TripForm(forms.ModelForm):
  class Meta:
    model = Trip
    fields = ['customer', 'driver', 'pickup_location', 'dropoff_location', 'airline', 'passengers', 'pickup_time', 'fare', 'payment_method', 'status']

class DriverForm(forms.ModelForm):
  class Meta:
    model = Driver
    fields = ['first_name', 'last_name', 'phone', 'vehicle_type', 'reliability', 'passenger_limit']


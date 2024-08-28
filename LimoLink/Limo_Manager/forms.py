from django import forms
from .models import Customer, Trip, Driver

class CustomerForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ['name', 'email', 'phone']

class TripForm(forms.ModelForm):
  class Meta:
    model = Trip
    fields = ['customer', 'driver', 'pickup_location', 'dropoff_location', 'airline', 'passengers', 'pickup_time', 'fare', 'payment_method', 'status']

class DriverForm(forms.ModelForm):
  class Meta:
    model = Driver
    fields = ['name', 'phone', 'vehicle_type', 'reliability', 'passenger_limit']

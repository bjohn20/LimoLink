from django.contrib import admin
from .models import Customer, Driver, Trip

# Register your models here.
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Trip)
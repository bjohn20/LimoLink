from django.contrib import admin

from .models import User, Client, Driver, Booking

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Driver)
admin.site.register(Booking)
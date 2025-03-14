from django.contrib import admin

from .models import User, Client, Driver, UserProfile

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Client)
admin.site.register(Driver)
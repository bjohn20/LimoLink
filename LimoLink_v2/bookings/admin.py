from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'client', 'pickup_street_address', 'pickup_city', 'pickup_state', 'pickup_zip_code',
        'dropoff_street_address', 'dropoff_city', 'dropoff_state', 'dropoff_zip_code',
        'pickup_time'
    )
    list_filter = ('pickup_city', 'dropoff_city', 'pickup_time')
    search_fields = ('client__name', 'pickup_street_address', 'dropoff_street_address')
    ordering = ('pickup_time',)
    fieldsets = (
        ('Client Information', {
            'fields': ('client',)
        }),
        ('Pickup Details', {
            'fields': ('pickup_street_address', 'pickup_city', 'pickup_state', 'pickup_zip_code', 'pickup_datetime')
        }),
        ('Drop-off Details', {
            'fields': ('dropoff_street_address', 'dropoff_city', 'dropoff_state', 'dropoff_zip_code')
        }),
    )

admin.site.register(Booking, BookingAdmin)

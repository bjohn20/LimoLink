from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('customers/', views.customers, name='customers'),
  path('customers/add/', views.add_customer, name='add_customer'),
  path('customers/<int:customner_id>/delete', views.delete_customer, name='delete_customer'),
  path('trips/', views.trips, name='trips'),
  path('trip/add/', views.add_trip, name='add_trip'),
  path('trip/<int:trip_id>/edit/', views.edit_trip, name='edit_trip'),
  path('trip/<int:trip_id>/delete/', views.delete_trip, name='delete_trip'),
  path('trip/<int:trip_id>/', views.trip_detail, name='trip_detail'),
  path('drivers/', views.drivers, name='drivers'),
  path('drivers/add/', views.add_driver, name='add_driver'),
  path('drivers/<int:driver_id>/delete', views.drivers, name='delete_drivers'),
]
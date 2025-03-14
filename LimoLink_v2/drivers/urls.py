from django.urls import path
from .views import DriverListView, DriverCreateView, DriverDetailView, DriverUpdateView, DriverDeleteView

app_name = 'drivers'

urlpatterns = [
  path('create/', DriverCreateView.as_view(), name="driver-create"),
  path('', DriverListView.as_view(), name="driver-list"),
  path('<int:pk>/', DriverDetailView.as_view(), name="driver-detail"),
  path('<int:pk>/update/', DriverUpdateView.as_view(), name="driver-update"),
  path('<int:pk>/delete/', DriverDeleteView.as_view(), name="driver-delete"),
]
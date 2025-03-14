from django.urls import path
from .views import BookingListView, BookingDetailView, BookingCreateView, BookingUpdateView, BookingDeleteView

app_name = 'bookings'

urlpatterns = [
    path('', BookingListView.as_view(), name="booking-list"),
    path('create/', BookingCreateView.as_view(), name="booking-create"),
    path('<int:pk>/delete/', BookingDeleteView.as_view(), name="booking-delete"),
    path('<int:pk>/', BookingDetailView.as_view(), name="booking-detail"),
    path('<int:pk>/update/', BookingUpdateView.as_view(), name="booking-update"),
]
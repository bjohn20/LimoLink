from email import message
from urllib import response
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Booking
from .forms import BookingForm

class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'
    paginate_by = 10
    
    def get_queryset(self):
      return Booking.objects.all()

class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = 'bookings/booking_detail.html'
    context_object_name = 'bookings'
    
    def get(self, request, *args, **kwargs):
      print(f"Debug: Booking Detail View called with PK={kwargs.get('pk')}")
      return super().get(request, *args, **kwargs)
  
    
class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    template_name = 'bookings/booking_create.html'
    form_class = BookingForm
    success_url = reverse_lazy('bookings:booking-list')
    
    def form_valid(self, form):
      form.instance.created_by = self.request.user
      response = super().form_valid(form)
      messages.success(self.request, "Booking created successfully")
      return response

class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    template_name = 'bookings/booking_update.html'
    form_class = BookingForm
    context_object_name = 'bookings'
    success_url = reverse_lazy('bookings:booking-list')
    
    def form_valid(self, form):
      messages.success(self.request, "Booking updated successfully")
      form.instance.updated_by = self.request.user
      return super().form_valid(form)

class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'bookings/booking_confirm_delete.html'
    success_url = reverse_lazy('bookings:booking-list')
    context_object_name = 'bookings'

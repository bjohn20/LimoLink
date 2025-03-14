from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView , DetailView
from .models import Driver
from .forms import DriverForm
from django.contrib import messages
from django.urls import reverse_lazy

class DriverCreateView(LoginRequiredMixin, CreateView):
    model = Driver
    template_name = 'drivers/driver_create.html'
    form_class = DriverForm
    success_url = reverse_lazy('drivers:driver-list')
    
    def form_valid(self, form):
        existing_driver = Driver.objects.filter(user=self.request.user).first()
        if existing_driver:
            messages.info(self.request, "You already have a driver profile. Redirecting to update it.")
            return redirect('drivers:driver-update', pk=existing_driver.pk)
        
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "Driver profile created successfully")
        return response
      
class DriverListView(LoginRequiredMixin, ListView):
    model = Driver
    template_name = 'drivers/driver_list.html'
    context_object_name = 'drivers'
    
class DriverDetailView(LoginRequiredMixin, DetailView):
    model = Driver
    template_name = 'drivers/driver_detail.html'
    context_object_name = 'drivers'
    
class DriverUpdateView(LoginRequiredMixin, UpdateView):
    model = Driver
    template_name = 'drivers/driver_update.html'
    form_class = DriverForm
    context_object_name = 'drivers'
    success_url = reverse_lazy('drivers:driver-list')
    
    def form_valid(self, form):
      messages.success(self.request, "Driver updated successfully")
      form.instance.updated_by = self.request.user
      return super().form_valid(form)
    
class DriverDeleteView(LoginRequiredMixin, DeleteView):
    model = Driver
    template_name = 'drivers/driver_confirm_delete.html'
    success_url = reverse_lazy('drivers:driver-list')
    context_object_name = 'drivers'

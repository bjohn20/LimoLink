from django.core.mail import send_mail
from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.views import generic
from .models import User, Driver, Client
from .forms import ClientForm, ClientModelForm


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = BaseUserCreationForm
    
    def get_success_url(self):
        return reverse("login")


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

def landing_page(request):
    return render(request, 'landing.html')

class ClientListView(LoginRequiredMixin, generic.ListView):
    template_name = "clients/client_list.html"
    queryset = Client.objects.all() 
    context_object_name = "clients"

def client_list(request):
    users = User.objects.all()
    drivers = Driver.objects.all()
    clients = Client.objects.all()
    context = {
        "users": users,
        "drivers": drivers,
        "clients": clients,
    }
    return render(request, 'clients/client_list.html', context)


class ClientDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "clients/client_detail.html"
    queryset = Client.objects.all() 
    context_object_name = "client"

def client_detail(request, pk):
    client = Client.objects.get(pk=pk)
    context = {
        "client": client,
    }
    return render(request, 'clients/client_detail.html', context)


class ClientCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "clients/client_create.html"
    form_class = ClientModelForm 

    def get_success_url(self):
        return reverse("clients:client-list")
    
    def form_valid(self, form):
        send_mail(
            subject="A Client has been created",
            message="Go to the site to see the new client",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(ClientCreateView, self).form_valid(form)

def client_create(request):
    form = ClientModelForm()
    if request.method == 'POST':
        form = ClientModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/clients")
    context = {
        "form": form
    }
    return render(request, 'clients/client_create.html', context)



class ClientUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "clients/client_update.html"
    queryset = Client.objects.all()
    form_class = ClientModelForm 

    def get_success_url(self):
        return reverse("clients:client-list")

def client_update(request, pk):
    client = Client.objects.get(pk=pk)
    form = ClientModelForm(instance=client)
    if request.method == 'POST':
        form = ClientModelForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("/clients")
    context = {
        "form": form,
        "client": client
    }
    return render(request, 'clients/client_update.html', context)


class ClientDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "clients/client_delete.html"
    queryset = Client.objects.all()

    def get_success_url(self):
        return reverse("clients:client-list")

def client_delete(request, pk):
    clients = Client.objects.get(pk=pk)
    clients.delete()
    return redirect("/clients")
    
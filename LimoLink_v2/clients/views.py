from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User, Driver, Client
from .forms import ClientForm, ClientModelForm

def landing_page(request):
    return render(request, 'landing.html')

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

def client_detail(request, pk):
    client = Client.objects.get(pk=pk)
    context = {
        "client": client,
    }
    return render(request, 'clients/client_detail.html', context)

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

def client_delete(request, pk):
    clients = Client.objects.get(pk=pk)
    clients.delete()
    return redirect("/clients")
    
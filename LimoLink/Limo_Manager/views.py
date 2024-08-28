from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomerForm, TripForm, DriverForm
from .models import Customer, Driver, Trip

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})

def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail', customer_id=customer.id)
        
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)

    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    
    return render(request, 'delete_customer.html', {'customer': customer})

def trips(request):
    trips = Trip.objects.all()
    return render(request, 'trips.html', {'trips': trips})

def trip_list(request):
    trips = Trip.objects.all()
    return render(request, 'trip_list.html', {'trips': trips})

def trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    return render(request, 'trip_detail.html', {'trip': trip})

def add_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trips')
    else:
        form = TripForm()
        
    return render(request, 'add_trip.html', {'form': form})
    
def edit_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)

    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('trip_detail', trip_id=trip.id)
    else:
        form = TripForm(instance=trip)
        
    return render(request, 'edit_trip.html', {'form': form, 'trip': trip})
    
def delete_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)

    if request.method == 'POST':
        trip.delete()
        return redirect('trip_list')
    
    return render(request, 'delete_trip.html', {'trip': trip})

def drivers(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers.html', {'drivers': drivers})

def add_driver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drivers')
    else:
        form = DriverForm()
    return render(request, 'add_driver.html', {'form': form})
    
def edit_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)

    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('driver_detail', driver_id=driver.id)
    else:
        form = DriverForm(instance=driver)

def delete_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)

    if request.method == 'POST':
        driver.delete()
        return redirect('driver_list')
    
    return render(request, 'delete_driver.html', {'driver': driver})



    


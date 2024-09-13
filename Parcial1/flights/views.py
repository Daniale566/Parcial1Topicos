from django.shortcuts import render, redirect
from .forms import FlightForm
from .models import Flight
from django.db.models import Avg

def index(request):
    return render(request, 'flights/index.html')

def list_flights(request):
    flights = Flight.objects.all().order_by('price')
    return render(request, 'flights/list_flights.html', {'flights': flights})

def flight_statistics(request):
    national_flights_count = Flight.objects.filter(flight_type='N').count()
    international_flights_count = Flight.objects.filter(flight_type='I').count()
    national_flights_avg_price = Flight.objects.filter(flight_type='N').aggregate(Avg('price'))['price__avg']

    context = {
        'national_flights_count': national_flights_count,
        'international_flights_count': international_flights_count,
        'national_flights_avg_price': national_flights_avg_price,
    }
    return render(request, 'flights/flight_statistics.html', context)

def register_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FlightForm()
    return render(request, 'flights/register_flight.html', {'form': form})
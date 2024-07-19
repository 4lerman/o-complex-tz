from django.shortcuts import render, redirect
from .forms import CityForm
from .models import WeatherQuery
from .utils import get_weather

def index(request):
    if request.method == "GET":
        form = CityForm(request.GET)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather = get_weather(city)

            if weather:
                query, created = WeatherQuery.objects.get_or_create(city=city)
                query.count += 1
                query.save()
                return render(request, 'result.html', {'weather': weather, 'city': city})
    else:
        form = CityForm()
    return render(request, 'index.html', {'form': form})

def history(request):
    queries = WeatherQuery.objects.all().order_by('-updatedAt')
    return render(request, 'history.html', {'queries': queries})


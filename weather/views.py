from django.shortcuts import render
from .models import WeatherData 
from django.utils.dateparse import parse_date
from django.views.generic import  CreateView, UpdateView, DeleteView
from .models import WeatherData
from .forms import WeatherDataForm, WeatherFilterForm
from django.urls import reverse_lazy
import csv
from django.http import HttpResponse
import csv
from django.conf import settings
from django.utils.timezone import now


def WeatherListView(request):
    weather_data = WeatherData.objects.all()
    city = request.GET.get('city')
    
    if city:
        weather_data = weather_data.filter(city__icontains=city)
    
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date:
        start_date = parse_date(start_date)
        weather_data = weather_data.filter(timestamp__date__gte=start_date)
    
    if end_date:
        end_date = parse_date(end_date)
        weather_data = weather_data.filter(timestamp__date__lte=end_date)
    return render(request, 'weather/weather_list.html', {'weather_data': weather_data})

class WeatherCreateView(CreateView):
    model = WeatherData
    form_class = WeatherDataForm
    template_name = 'weather/weather_form.html'
    success_url = reverse_lazy('weather_list')

class WeatherUpdateView(UpdateView):
    model = WeatherData
    form_class = WeatherDataForm
    template_name = 'weather/weather_form.html'
    success_url = reverse_lazy('weather_list')

class WeatherDeleteView(DeleteView):
    model = WeatherData
    template_name = 'weather/weather_confirm_delete.html'
    success_url = reverse_lazy('weather_list')

def FilteredWeatherListViewForCsv(request):
    form = WeatherFilterForm(request.GET)
    
    if form.is_valid():
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')
        city = form.cleaned_data.get('city')
        
        queryset = WeatherData.objects.all()
        
        if start_date:
            queryset = queryset.filter(timestamp__gte=start_date)
        if end_date:
            queryset = queryset.filter(timestamp__lte=end_date)
        if city:
            queryset = queryset.filter(city__icontains=city)
        
        # Create a CSV file in memory
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="weather_data_{now().strftime("%Y%m%d_%H%M%S")}.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['City', 'Temperature (°C)', 'Humidity (%)', 'Description', 'Timezone', 'Timestamp'])
        
        for weather in queryset:
            writer.writerow([
                weather.city,
                weather.temperature,
                weather.humidity,
                weather.description,
                weather.timezone,
                weather.timestamp,
            ])
        
        return response

    return HttpResponse("Invalid form data", status=400)

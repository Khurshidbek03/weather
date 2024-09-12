from django import forms
from .models import WeatherData

class WeatherDataForm(forms.ModelForm):
    class Meta:
        model = WeatherData
        fields = ['city', 'temperature', 'humidity', 'description', 'timezone']

class WeatherFilterForm(forms.Form):
    start_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    city = forms.CharField(max_length=100, required=False)
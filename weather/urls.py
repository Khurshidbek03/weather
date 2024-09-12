from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.WeatherListView, name='weather_list'),
    path('filter/', views.FilteredWeatherListViewForCsv, name='weather_filtered_csv'),
    path('add/', views.WeatherCreateView.as_view(), name='weather_add'),
    path('<int:pk>/edit/', views.WeatherUpdateView.as_view(), name='weather_edit'),
    path('<int:pk>/delete/', views.WeatherDeleteView.as_view(), name='weather_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

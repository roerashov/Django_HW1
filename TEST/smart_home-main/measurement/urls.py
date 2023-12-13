from django.urls import path
from .views import SensorView, MeasurementView, OneSensorView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensor/<pk>/', OneSensorView.as_view()),
]
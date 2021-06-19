 
from django.urls import path
from . import views
urlpatterns = [
    path('raspberrypiserver/', views.sendSensorData),
     path('getData/', views.getSensorData),
    path('raspberrypiserver/<int:device_id>/', views.sendSensorDataById),
]



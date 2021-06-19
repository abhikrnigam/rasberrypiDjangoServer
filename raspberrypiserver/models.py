from django.db import models
import RPi.GPIO as GPIO
import time

channel=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)

def getSoilMoisture(channel):
    moisture = GPIO.input(channel)
    return moisture

# Create your models here.
class sensorData(models.Model):
    device_id = models.CharField(max_length=10)
    device_type = models.CharField(max_length=50)
    waterNeeded = str(getSoilMoisture(channel))
    
    
def __str__(self):
    return self.device_id
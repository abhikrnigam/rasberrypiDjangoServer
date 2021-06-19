from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import sensorDataSerializer
from .models import sensorData
import RPi.GPIO as GPIO
import time



channel=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)

device_id=9910256178

def getSoilMoisture(channel):
    moisture = GPIO.input(channel)
    return moisture


# Create your views here.
@api_view(['GET','PUT'])
def sendSensorData(request):
    if request.method == 'GET':
        obj = sensorData.objects.all()
        serializer = sensorDataSerializer(obj,many=True)
        print(serializer.data[1]['waterNeeded'])
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    elif request.method == 'POST':
        serializer = sensorDataSerializer(data=request.data,many=True)
        if serializers.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        
        
@api_view(['GET'])
def getSensorData(request):
    if request.method == 'GET':
        waterNeeded = int(getSoilMoisture(channel))
        device_type = 'raspberrypi4'
        context = {
            'waterNeeded':waterNeeded,
            'device_type':device_type,
            'device_id':device_id,
            }
        return Response(context,status=status.HTTP_201_CREATED)
        
@api_view(['GET'])        
def sendSensorDataById(request,device_id):
    try:
        obj = sensorData.objects.get(id=device_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = sensorDataSerializer(obj)
    return Response(serializer.data,status=status.HTTP_200_OK)

        
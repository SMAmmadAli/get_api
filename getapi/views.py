from django.shortcuts import render
from .models import Device
from .serializers import DeviceSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.

def DeviceDetail(request):
    all_device = Device.objects.all()
    serializer = DeviceSerializer(all_device, many = True)
    return JsonResponse(serializer.data, safe=False)

from django.contrib import admin
from django.urls import path
from getapi import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('device/', views.DeviceDetail)
]

from django.contrib import admin
from django.urls import path
from decrypt import views
 
urlpatterns = [
    path('', views.decrypt, name='decrypt'),
]     
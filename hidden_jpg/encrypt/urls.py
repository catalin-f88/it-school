from django.contrib import admin
from django.urls import path
from encrypt import views
 
urlpatterns = [
    path('', views.encrypt, name='encrypt'),
]     
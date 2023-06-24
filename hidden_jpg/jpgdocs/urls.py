from django.urls import path
from jpgdocs import views
 
urlpatterns = [
    path('', views.docs, name='docs'),
]     
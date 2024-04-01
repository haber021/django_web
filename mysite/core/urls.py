from django.urls import path
from . import views

app_name = 'expenses'  # Define the app namespace


urlpatterns = [
    path('', views.index, name='index'),  
]
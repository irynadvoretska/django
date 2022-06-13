from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("iryna", views.iryna, name="iryna")
    ]

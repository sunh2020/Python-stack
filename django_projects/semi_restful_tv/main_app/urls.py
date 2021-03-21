from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    # path("shows", views.dashboard),
    path("shows/create", views.create),
    # path("shows/new", views.newShow),
    
  
]
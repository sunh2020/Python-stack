from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("shows", views.dashboard),
    path("shows/new", views.addShow),
    path("shows/create", views.create),
    path("shows/<int:show_id>", views.displayShow),
    path("shows/<int:show_id>/edit", views.editShow),
    path("shows/<int:show_id>/update", views.updateShow),
    path("shows/<int:show_id>/destory", views.deleteShow)
    
]
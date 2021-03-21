from django.urls import path
from . import views

urlpatterns = [
    path("login", views.index),
    path("destory_session", views.create),
    path("reset", views.reset)
]
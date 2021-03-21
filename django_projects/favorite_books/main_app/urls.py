from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("register", views.register),
    path("books", views.books),
    path("add_book", views.add_book),
    path("books/<int:id>", views.created),
    path("book_details", views.book_details),
    path("login", views.login),
    path("logout", views.logout)
   
]    
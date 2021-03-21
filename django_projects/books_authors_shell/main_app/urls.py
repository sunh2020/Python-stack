from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("author2", views.author2),
    path("books", views.add_book),
    path("authors", views.add_author),
    path("result_book/<int:id>", views.result_book),
    path("result_author/<int:id>", views.result_author),
    path("addBook", views.addBook),
    path("addAuthor", views.addAuthor)

]
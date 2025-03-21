from django.urls import path
from .views import home, movie_list, movie_add, movie_edit, movie_delete  # Ensure 'movie_add' is present

urlpatterns = [
    path("", home, name="home"),
    path("list/", movie_list, name="movie_list"),
    path("add/", movie_add, name="movie_add"),
    path("edit/<int:pk>/", movie_edit, name="movie_edit"),
    path("delete/<int:pk>/", movie_delete, name="movie_delete"),
]

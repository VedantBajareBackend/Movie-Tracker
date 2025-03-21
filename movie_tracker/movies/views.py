from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import MovieForm  # Ensure this line is present
from .models import Movie  # Assuming you have a Movie model


def home(request):
    return HttpResponse("<h1>Welcome to Movie Tracker</h1><p><a href='/movies/'>View Movies</a></p>")

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "movies/list.html", {"movies": movies})

def movie_add(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movie_list")  # Ensure this matches the URL name
    else:
        form = MovieForm()

    return render(request, "movies/movie_add.html", {"form": form})
def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movie_list")  # Redirect to the movie list page
    else:
        form = MovieForm()

    return render(request, "movies/add_movie.html", {"form": form})

def movie_edit(request, id):
    return HttpResponse(f"Edit Movie Page for ID {id} (Form coming soon)")

def movie_delete(request, id):
    return HttpResponse(f"Delete Movie with ID {id} (Confirmation coming soon)")

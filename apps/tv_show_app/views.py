from django.shortcuts import render, redirect
from .models import Movie
from django.contrib import messages

def index(request):
    all_movies = Movie.objects.all()
    print(request.session['id'])
    return render(request, 'tv_show_app/index.html', {'all_movies': all_movies})

def new(request):
    return render(request, 'tv_show_app/new.html')

def create(request):
    errors = Movie.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/shows/new')
    else:
        movie = Movie.objects.create(title=request.POST['title'], network=request.POST['network'], air_date=request.POST['air_date'], description=request.POST['description'])
    return redirect(f"/shows/{movie.id}")

def show(request, number):
    movie = Movie.objects.get(id=number)
    context = {
        "movie": movie
    }
    return render(request, 'tv_show_app/show.html', context)

def destroy(request, number):
    movie = Movie.objects.get(id=number)
    context = {
        "movie": movie
    }
    if movie:
        movie.delete()
    return redirect('/shows')

def update(request, number):
    errors = Movie.objects.validator(request.POST)
    movie = Movie.objects.get(id=number)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect(f"/shows/{movie.id}/edit")
    else:
        movie.title = request.POST['title']
        movie.network = request.POST['network']
        movie.air_date = request.POST['air_date']
        movie.description = request.POST['description']
        movie.save()
    return redirect(f'/shows/{movie.id}')

def edit(request, number):
    movie = Movie.objects.get(id=number)
    print(type(movie.air_date))
    context = {
        "movie": movie,
        "date": str(movie.air_date)
    }
    return render(request, 'tv_show_app/edit.html', context)
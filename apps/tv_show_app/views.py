from django.shortcuts import render, redirect
from .models import Movie

def index(request):
    all_movies = Movie.objects.all()
    print(request.session['id'])
    return render(request, 'tv_show_app/index.html', {'all_movies': all_movies})

def new(request):
    return render(request, 'tv_show_app/new.html')

def create(request):
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
    movie = Movie.objects.get(id=number)
    # context = {
    #     "movie": movie,
    #     "updated_title": request.POST['title'],
    #     "updated_network": request.POST['network'],
    #     "updated_date": request.POST['air_date'],
    #     "updated_desc": request.POST['description']
    # }
    # movie.title = updated_title
    # movie.network = updated_network
    # movie.air_date = updated_date
    # movie.description = updated_desc
    movie.title = request.POST['title']
    movie.save()
    movie.network = request.POST['network']
    movie.save()
    movie.air_date = request.POST['air_date']
    movie.save()
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
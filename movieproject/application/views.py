from django.shortcuts import render
from application.models import Movie
from application.forms import MovieForm
# Create your views here.
def index_view(request):
    return render(request,'application/index.html')

def movies_list_view(request):
    movies_list=Movie.objects.all()
    return render(request,'application/listmovies.html',{'movies_list':movies_list})

def add_movie_view(request):
    form=MovieForm()
    if request.method == "POST":
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return index_view(request)
    return render(request,'application/addmovie.html',{'form':form})
    
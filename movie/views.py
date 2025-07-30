from django.http import HttpResponse
from .models import Movie
# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'David'})

def about(request):
    return HttpResponse('<h1>Welcome to about Page</h1>')

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies})

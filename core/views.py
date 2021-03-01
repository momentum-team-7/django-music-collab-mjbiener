from django.shortcuts import render
from .models import Album
from .models import Artist
from .models import Home

# Create your views here.

def home(request):
    return render(request, 'project/index.html')


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'project/album.html', {'albums': albums})

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'project/artist.html', {'artists': artists})
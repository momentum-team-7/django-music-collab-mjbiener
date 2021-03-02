from django.shortcuts import render, get_object_or_404
from .models import Album, Artist, Home


# Create your views here.

def home(request):
    return render(request, 'project/index.html')


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'project/album.html', {'albums': albums})

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'project/artist.html', {'artists': artists})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'project/album-detail.html', {'album': album})

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'project/artist-detail.html', {'artist': artist})
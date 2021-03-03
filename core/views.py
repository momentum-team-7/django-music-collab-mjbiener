from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Album, Artist, Home
from .forms import ArtistForm, AlbumForm


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



def add_artist(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ArtistForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ArtistForm()

    return render(request, 'project/add-artist.html', {'form': form})


def add_album(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
    
        # create a form instance and populate it with data from the request:
        form = AlbumForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AlbumForm()

    return render(request, 'project/add-album.html', {'form': form})
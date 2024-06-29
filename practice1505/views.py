from django.shortcuts import render
from musician.models import Musician
from album.models import Album
# Create your views here.
def home(request):
    musician = Musician.objects.all()
    album = Album.objects.all()
    return render(request,'homepage.html',{'musician':musician,'album':album})
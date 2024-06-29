from django.shortcuts import render,redirect
from .forms import AlbumForm
from . import models
# from . import 
# Create your views here.
def album(request):
    if request.method=='POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album')
    else:
        form = AlbumForm()
        
    return render(request,'album.html',{'form':form})


def edit_post(request,id):
    post = models.Album.objects.get(pk=id)
    form = AlbumForm(instance = post)
    if request.method=='POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            return redirect('homepage')
    return render(request,'album.html',{'form':form})


def delete_post(request,id):
    target = models.Album.objects.get(pk=id)
    target.delete()
    return redirect('homepage')
    

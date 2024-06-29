from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def musician(request):
    if request.method =='POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musician')
    else:
        form = forms.MusicianForm()
    print(form)
    return render(request,'musician.html',{'form':form})


def edit_musician(request, id):
    target = models.Musician.objects.get(pk=id)
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=target)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = forms.MusicianForm(instance=target)
    
    return render(request, 'musician.html', {'form': form})

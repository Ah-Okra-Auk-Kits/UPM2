from django.shortcuts import render, redirect
from .forms import MusicForm
from .models import Music

def home(request):
    musics = Music.objects.all()
    return render(request, 'musicup/home.html', {'musics': musics})

def upload(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MusicForm()
    return render(request, 'musicup/upload.html', {'form': form})

def delete_music(request, pk):
    music = Music.objects.get(pk=pk)
    music.delete()
    return redirect('home')

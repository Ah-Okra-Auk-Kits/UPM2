from django.shortcuts import render, redirect
from .forms import MusicForm
from .models import Music
from django.shortcuts import get_object_or_404

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
    music = get_object_or_404(Music, pk=pk)
    if request.method == 'POST':
        music.delete()
        return redirect('home')
    return render(request, 'musicup/delete_music.html', {'music': music})

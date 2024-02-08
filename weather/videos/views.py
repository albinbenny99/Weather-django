from django.shortcuts import render
from .models import Video

def videos_list(request):
    videos = Video.objects.all()
    return render(request, 'videos_list.html', {'videos': videos})

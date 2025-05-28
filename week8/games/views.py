from django.shortcuts import render, get_object_or_404
from .models import VideoGame

def game_list(request):
    games = VideoGame.objects.all()
    return render(request, 'games/list.html', {'games': games})

def game_detail(request, game_id):
    game = get_object_or_404(VideoGame, id=game_id)
    return render(request, 'games/detail.html', {'game': game})



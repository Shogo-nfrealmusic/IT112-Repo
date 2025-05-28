from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('games/<int:game_id>/', views.game_detail, name='game_detail'),
]

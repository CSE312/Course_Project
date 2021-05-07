## urls.py
from django.urls import path
from .views import index, game

urlpatterns = [
    path('', index),
    path('play/<room_code>', game),
]
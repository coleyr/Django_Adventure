from django.urls import path, include
from . import views
from .utils import get_images, get_audio, get_video

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:adventure>/about', views.adventure_about, name='adventure_about'),
    path('<str:adventure>/clue/<str:name>', views.clue, name='clue'),
    path('about', views.about, name='about')
]

get_images()
get_audio()
get_video()
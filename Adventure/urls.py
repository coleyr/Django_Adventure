from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('<str:adventure>/begin', views.startmessage),
    path('<str:adventure>/clue', views.clue),
    path('about', views.about)
]

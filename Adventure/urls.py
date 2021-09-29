from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:adventure>/about', views.adventure_about, name='adventure_about'),
    path('<str:adventure>/clue/<str:name>', views.clue, name='clue'),
    path('about', views.about, name='about')
]

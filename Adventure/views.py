from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import StartingMessage, Adventure, Clue
# Create your views here.

def startmessage(request, adventure):
    StartMessage = StartingMessage.objects.get(adventure__name__contains=adventure)
    audio = StartMessage.audio.audiofile.url or ""
    message = StartMessage.message_text or ""
    display = StartMessage.display.name
    template = loader.get_template(f'home/{display}.html') if display else loader.get_template(f'home/console_typing.html') 
    context = {
        'message': message,
        'audio': audio
    }
    return HttpResponse(template.render(context, request))

def clue(request, adventure):
    clue = Clue.objects.get(adventure__name__contains=adventure)
    audio = clue.audio.audiofile.url if clue.audio else ""
    display = clue.display.name
    template = loader.get_template(f'clues/{display}.html')
    context = {
        'audio': audio
    }
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('home/index.html')
    context = {
        'message': ":)",
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('home/about.html')
    context = {
        'message': ":)",
    }
    return HttpResponse(template.render(context, request))


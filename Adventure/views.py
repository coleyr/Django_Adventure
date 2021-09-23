from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import StartingMessage, Adventure, Clue
# Create your views here.
adventure_image_urls = {adventure.name: [adventure.image.imagefile.url, adventure.description] for adventure in Adventure.objects.all() if adventure.image}

def getnext(clue, adventure):
    try:
        next_clue = Clue.objects.get(adventure__name__contains=adventure, clueorder=clue.clueorder + 1)
        return next_clue.name
    except:
        print("NO NEXT CLUE")
        return ""
    

def startmessage(request, adventure):
    StartMessage = StartingMessage.objects.get(adventure__name__contains=adventure)
    firstclue = Clue.objects.get(adventure__name__contains=adventure, clueorder__contains='1').name
    audio = StartMessage.audio.audiofile.url if StartMessage.audio else ""
    message = StartMessage.message_text or ""
    template = (loader.get_template(f'home/{StartMessage.display.name}.html')
                if StartMessage.display
                else loader.get_template('home/console_typing.html'))
    context = {
        'message': message,
        'audio': audio,
        'cluename': firstclue,
        'adventure': adventure
    }
    return HttpResponse(template.render(context, request))

def clue(request, adventure, name):
    given_answer = request.GET.get("answer", "")
    clue = Clue.objects.get(adventure__name__contains=adventure, name__contains=name)
    correct_answer = clue.answer
    audio = clue.audio.audiofile.url if clue.audio else ""
    display = clue.display.name
    template = (f'clues/{display}.html')
    next_clue_name = ""
    if given_answer == correct_answer:
        next_clue_name = getnext(clue, adventure)
    context = {
        'audio': audio,
        'adventure': adventure,
        'next': next_clue_name
    }
    return render(request, template, context)


def home(request):
    template = 'home/index.html'
    context = {
        'adventures': adventure_image_urls
    }

    return render(request, template, context)

def about(request):
    template = loader.get_template('home/about.html')
    context = {
        'message': ":)",
    }
    return HttpResponse(template.render(context, request))


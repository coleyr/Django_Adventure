from django.shortcuts import render, HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Adventure, Clue, Hint
# Create your views here.

def get_adventures():
    adventures = {}
    for adventure in Adventure.objects.all():
        try:
            FirstClueName = Clue.objects.get(adventure__name__contains=adventure, clueorder=1).name
            clueurl = reverse('clue', kwargs={'name': FirstClueName, 'adventure': adventure})
        except:
            clueurl = "#NO FIRST CLUE"
        image = adventure.image.imagefile.url if adventure.image else ""
        adventures[adventure.name] = {
        "image": image,
        "description": adventure.description,
        "clueurl": clueurl
        }

    return adventures

def getnext(clue, adventure):
    try:
        next_clue = Clue.objects.get(adventure__name__contains=adventure, clueorder=clue.clueorder + 1)
        clueurl = reverse('clue', kwargs={'name': next_clue.name, 'adventure': adventure})
        return clueurl
    except:
        return ""

def getcluehints(clue):
    hint_objs = Hint.objects.filter(clue=clue)
    character_name = clue.character_name
    hints = makehintpage(hint_objs, character_name)
    return hints


def makehintpage(hints, character_name):
    hinthtmllist = []
    for hint in hints:
        message = hint.hint_message
        audio = hint.audio.audiofile.url if hint.audio else ""
        video = hint.video.videofile.url if hint.video else ""
        image = hint.image.imagefile.url if hint.image else ""
        displaycontext = {'message': message,'audio': audio, 'video': video, 'image': image, "character_name": character_name}
        displayhinthtml = loader.render_to_string("clues/hints.html", displaycontext)
        hinthtmllist.append(displayhinthtml)
    return hinthtmllist

def getcurrent(clue, adventure):
    try:
        current_clue = Clue.objects.get(adventure__name__contains=adventure, clueorder=clue.clueorder)
        clueurl = reverse('clue', kwargs={'name': current_clue.name, 'adventure': adventure})
        return clueurl
    except:
        return "#"

def clue(request, adventure, name):
    clue = Clue.objects.get(adventure__name__contains=adventure, name__contains=name)
    given_answer = request.GET.get("answer", "")
    correct_answer = clue.answer == given_answer
    cluename = clue.name
    message = clue.message
    character_name = clue.character_name
    audio = clue.audio.audiofile.url if clue.audio else ""
    video = clue.video.videofile.url if clue.video else ""
    image = clue.image.imagefile.url if clue.image else ""
    hints = getcluehints(clue)
    displaycontext = {'message': message,'audio': audio, 'video': video, 'image': image, "character_name": character_name, "answer": given_answer}
    displayhtml = loader.render_to_string("clues/display.html", displaycontext)
    inputcontext = {"answer": given_answer}
    inputhtml = loader.render_to_string("clues/input.html", inputcontext)
    absolute_url = request.build_absolute_uri(getcurrent(clue, adventure))
    if correct_answer:
        nextclue = getnext(clue, adventure) or ""
        displaycontext = {'message': clue.success_message, 'audio': "", 'video': "", 'image': "", "character_name": character_name, "answer": "correct", 'nextclue': nextclue}
        displayhtml = loader.render_to_string("clues/display.html", displaycontext)
        context = {
        'adventure': adventure,
        'cluename': cluename,
        'display': displayhtml,
        'input': f"<h2 class='text-center mt-0'>Correct Answer: {given_answer}</h2>",
        'saveurl': absolute_url
    }
        return render(request, "clues/basic.html", context)
    context = {
        'adventure': adventure,
        'cluename': cluename,
        'display': displayhtml,
        'input': inputhtml,
        'saveurl': absolute_url,
        'hints': hints
    }
    return render(request, "clues/basic.html", context)


def home(request):
    template = 'home/index.html'
    context = {
        'adventures': get_adventures()
    }

    return render(request, template, context)

def about(request):
    template = loader.get_template('home/about.html')
    context = {
        'message': ":)",
    }
    return HttpResponse(template.render(context, request))


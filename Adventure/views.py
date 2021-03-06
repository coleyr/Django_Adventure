from typing import List
from django.db.models.query import QuerySet
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Adventure, Clue, Hint, Image, Video, Audio, Map

# Create your views here.
def getfirstclue(adventure):
    try:
        FirstClueName = Clue.objects.get(adventure__name__contains=adventure, clueorder=1).name
        clueurl = reverse('clue', kwargs={'name': FirstClueName, 'adventure': adventure})
    except:
        clueurl = "#NO FIRST CLUE"
    return clueurl

def abbrieviate(message: str):
    if len(message) > 100:
        return message[0:100] + "..."
    else:
        return message

def get_adventures():
    adventures = {}
    for adventure in Adventure.objects.all():
        image = adventure.image.url if adventure.image else ""
        try:
            abouturl = reverse('adventure_about', kwargs={'adventure': adventure})
        except:
            abouturl = "#NO FIRST CLUE"
        adventures[adventure.name] = {
        "image": image,
        "description": abbrieviate(adventure.description),
        "abouturl": abouturl,
        "location": adventure.location,
        "clueurl": getfirstclue(adventure)
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

def getmedia(clue):
    # I know this is long form but it is easier to know
    # what the heck this is doing
    image, audio, video, map = {}, {}, {}, {}
    clue_imgs = Image.objects.filter(clue=clue)
    clue_audio = Audio.objects.filter(clue=clue)
    clue_video = Video.objects.filter(clue=clue)
    clue_maps = Map.objects.filter(clue=clue)
    for img in clue_imgs:
        image[img.name] = img.imagefile.url
    for vid in clue_video:
        video[vid.name] = vid.videofile.url
    for aud in clue_audio:
        audio[aud.name] = aud.audiofile.url
    for map in clue_maps:
        map = {'lat':map.lat, 'lng':map.lng, 'radius':map.radius, 'required':map.required}
    return image, audio, video, map

def makehintpage(hints: QuerySet, character_name: str):
    hinthtmllist = []
    for hint in hints:
        message = hint.hint_message
        audio = hint.audio.audiofile.url if hint.audio else ""
        video = hint.video.videofile.url if hint.video else ""
        image = hint.image.imagefile.url if hint.image else ""
        displaycontext = {'message': message,
        'audio': audio, 
        'video': video,
        'image': image,
        "character_name": character_name}
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
    clue = Clue.objects.get(adventure__name__contains=adventure, name=name)
    given_answer = request.GET.get("answer", "")
    correct_answer = clue.answer.lower() == given_answer.lower()
    cluename = clue.name
    character_name = clue.character_name
    absolute_url = request.build_absolute_uri(getcurrent(clue, adventure))
    if correct_answer:
        nextclue = getnext(clue, adventure) or ""
        displaycontext = {'message': clue.success_message, 'audio': "", 'video': "", 'image': "", 'map': "", "character_name": character_name, "answer": "correct", 'nextclue': nextclue}
        displayhtml = loader.render_to_string("clues/display.html", displaycontext)
        context = {
        'adventure': adventure,
        'cluename': cluename,
        'display': displayhtml,
        'input': f"<h2 class='text-center mt-0'>Correct Answer: {given_answer}</h2>",
        'saveurl': absolute_url
    }
        return render(request, "clues/basic.html", context)
    message = clue.message
    image, audio, video, map = getmedia(clue)
    maphtml = loader.render_to_string("clues/map.html", map) if map else ""
    hints = getcluehints(clue)
    displaycontext = {'message': message,'audio': audio, 'video': video, 'image': image, "character_name": character_name, "answer": given_answer, "map":maphtml}
    displayhtml = loader.render_to_string("clues/display.html", displaycontext)
    inputcontext = {"answer": given_answer}
    inputhtml = loader.render_to_string("clues/input.html", inputcontext)
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

def get_adventure_info(adventure):
    adv = Adventure.objects.get(name=adventure)
    return {"name": adv.name, "description": adv.description, "image": adv.image.url, "location": adv.location, "clueurl": getfirstclue(adventure)}

def adventure_about(request, adventure):
    context = {
        'adv_info': get_adventure_info(adventure),
    }
    return render(request, "home/adventure_about.html", context)

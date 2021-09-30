from os import listdir
from os import path
from django.conf import settings
from os.path import isfile, join
from .models import Audio, Image, Video

def get_images():
    mypath = f"{settings.MEDIA_ROOT}/images"
    imgfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for img in imgfiles:
        obj, created = Image.objects.get_or_create(
            imagefile = f"images/{img}")
        if created:
            obj.name = path.splitext(img)[0]
            obj.save()

def get_video():
    mypath = f"{settings.MEDIA_ROOT}/video"
    vidfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for vid in vidfiles:
        obj, created = Video.objects.get_or_create(
            videofile = f"viedo/{vid}")
        if created:
            obj.name = path.splitext(vid)[0]
            obj.save()

def get_audio():
    mypath = f"{settings.MEDIA_ROOT}/audio"
    audfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for aud in audfiles:
        obj, created = Audio.objects.get_or_create(
            audiofile = f"audio/{aud}")
        if created:
            obj.name = path.splitext(aud)[0]
            obj.save()
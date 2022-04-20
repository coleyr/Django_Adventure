from django.contrib import admin
from django.contrib.admin.helpers import Fieldline
from django.core.exceptions import ViewDoesNotExist
from .models import Adventure,  Audio, ClueOrder, Image, Clue, Video, Hint, Map


# Register your models here.

class HintInline(admin.TabularInline):
    model = Hint
    classes = ['extrapretty','collapse']
class ImageInline(admin.TabularInline):
    model = Image
    classes = ['extrapretty','collapse']
class VideoInline(admin.TabularInline):
    model = Video
    classes = ['extrapretty','collapse']

class AudioInline(admin.TabularInline):
    model = Audio
    classes = ['extrapretty','collapse']
class MapInline(admin.TabularInline):
    model = Map
    classes = ['extrapretty','collapse']
class ClueAdmin(admin.ModelAdmin):
    inlines = [
        MapInline,
        ImageInline,
        VideoInline,
        AudioInline,
        HintInline,
    ]



admin.site.register(Adventure)
admin.site.register(Audio)
admin.site.register(Image)
admin.site.register(Clue, ClueAdmin)
admin.site.register(Video)
admin.site.register(Map)
# admin.site.register(Hint)

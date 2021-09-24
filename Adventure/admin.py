from django.contrib import admin
from .models import Adventure,  Audio, Image, Clue, Video
# Register your models here.

admin.site.register(Adventure)
admin.site.register(Audio)
admin.site.register(Image)
admin.site.register(Clue)
admin.site.register(Video)


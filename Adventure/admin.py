from django.contrib import admin
from .models import Adventure, StartingMessage, Audio, Image, MessageDisplay, Clue, ClueDisplay
# Register your models here.

admin.site.register(Adventure)
admin.site.register(StartingMessage)
admin.site.register(Audio)
admin.site.register(Image)
admin.site.register(MessageDisplay)
admin.site.register(ClueDisplay)
admin.site.register(Clue)


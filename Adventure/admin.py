from django.contrib import admin
from django.contrib.admin.helpers import Fieldline
from .models import Adventure,  Audio, Image, Clue, Video, Hint
# Register your models here.

class HintInline(admin.TabularInline):
    model = Hint

class ClueAdmin(admin.ModelAdmin):
    inlines = [
        HintInline,
    ]



admin.site.register(Adventure)
admin.site.register(Audio)
admin.site.register(Image)
admin.site.register(Clue, ClueAdmin)
admin.site.register(Video)
# admin.site.register(Hint)

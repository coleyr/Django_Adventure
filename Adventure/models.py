from django.db import models
from django.core.validators import validate_slug
from django.core.exceptions import ValidationError
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
import os


#Validation for upload
def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpeg','.jpg','.gif', '.png']
    if not ext in valid_extensions:
        raise ValidationError(u"File Type '%s' not supported!\nThe file type must be %s" % (ext, ", ".join(valid_extensions)))

def validate_video_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp4']
    if not ext in valid_extensions:
        raise ValidationError(u"File Type '%s' not supported!\nThe file type must be %s" % (ext, ", ".join(valid_extensions)))

def validate_audio_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp3']
    if not ext in valid_extensions:
        raise ValidationError(u"File Type '%s' not supported!\nThe file type must be %s" % (ext, ", ".join(valid_extensions)))

# Create your models here.
class Adventure(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    location = models.CharField(max_length=128, default="No Specific Location")
    image = models.FileField(upload_to='images', default='images/default.jpg')
    def __str__(self):
        return f'{self.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='adventure_name_constraint')
        ]

ClueOrder = models.IntegerChoices('ClueOrder', 'FIRST SECOND THIRD FOURTH FIFTH SIXTH SEVENTH EIGHTH NINTH TENTH ELEVENTH TWELFTH THIRTEENTH FOURTEENTH FIFTEENTH')
class Clue(models.Model):
    name = models.CharField(max_length=100)
    character_name = models.CharField(max_length=100, default="Det. Ace Palmer")
    message = models.TextField(max_length=1000, default="Enter message here")
    success_message = models.TextField(max_length=1000, default="Enter message to be displayed on successful entry of answer")
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE, related_query_name="adventure")
    answer = models.CharField(max_length=100)
    clueorder = models.IntegerField(choices=ClueOrder.choices)

    def __str__(self):
        return f'{self.adventure.name} - Clue{self.clueorder}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['adventure', 'clueorder'], name='clue_adventure_constraint')
        ]

class Image(models.Model):
    imagefile = models.FileField(upload_to='images', validators=[validate_image_extension])
    name = models.CharField(max_length=100)
    clue = models.ForeignKey(Clue, on_delete=models.SET_NULL, related_query_name="clue", blank=True, null=True)

    
    def __str__(self):
        return f'{self.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['imagefile'], name='imagefile_unique_constraint')
        ]





class Audio(models.Model):
    audiofile = models.FileField(upload_to='audio', validators=[validate_audio_extension])
    name = models.CharField(max_length=100)
    clue = models.ForeignKey(Clue, on_delete=models.SET_NULL, related_query_name="clue", blank=True, null=True)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['audiofile'], name='audiofile_unique_constraint')
        ]


class Video(models.Model):
    videofile = models.FileField(upload_to='video', validators=[validate_video_extension])
    name = models.CharField(max_length=100)
    clue = models.ForeignKey(Clue, on_delete=models.SET_NULL, related_query_name="clue", blank=True, null=True)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['videofile'], name='videofile_unique_constraint')
        ]
  

class Hint(models.Model):
    name = models.CharField(max_length=200, validators=[validate_slug])
    audio = models.ForeignKey(Audio, on_delete=models.SET_NULL, related_query_name="audio", blank=True, null=True)
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, related_query_name="video", blank=True, null=True)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, related_query_name="image", blank=True, null=True)
    hint_message = models.TextField(max_length=500)
    clue = models.ForeignKey(Clue, on_delete=models.CASCADE, related_query_name="clue", blank=True, null=True)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['clue', 'name'], name='hint_name_constraint')
        ]
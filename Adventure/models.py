from django.db import models
from django.core.validators import validate_slug
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL

# Create your models here.
class Adventure(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
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
    imagefile = models.FileField(upload_to='images')
    name = models.CharField(max_length=100)
    clue = models.ForeignKey(Clue, on_delete=models.SET_NULL, related_query_name="clue", blank=True, null=True)

    
    def __str__(self):
        return f'{self.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['imagefile'], name='imagefile_unique_constraint')
        ]





class Audio(models.Model):
    audiofile = models.FileField(upload_to='audio')
    name = models.CharField(max_length=100)
    clue = models.ForeignKey(Clue, on_delete=models.SET_NULL, related_query_name="clue", blank=True, null=True)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['audiofile'], name='audiofile_unique_constraint')
        ]


class Video(models.Model):
    videofile = models.FileField(upload_to='video')
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
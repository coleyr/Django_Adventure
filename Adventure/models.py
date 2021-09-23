from django.db import models
from django.core.validators import validate_slug
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL

# Create your models here.
class Image(models.Model):
    imagefile = models.FileField(upload_to='images')
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['imagefile'], name='imagefile_unique_constraint')
        ]

# def get_default_image():
#     return Image.objects.get(name="default")

class Adventure(models.Model):
    name = models.CharField(max_length=200, validators=[validate_slug])
    image = models.ForeignKey(Image, on_delete=SET_NULL, related_query_name="image", null=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='adventure_name_constraint')
        ]

class Audio(models.Model):
    audiofile = models.FileField(upload_to='audio')
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['audiofile'], name='audiofile_unique_constraint')
        ]


class MessageDisplay(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='message_type_constraint')
        ]
        verbose_name = 'Message Type'
        verbose_name_plural = 'Message Types'   

class ClueDisplay(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='clue_type_constraint')
        ]
        verbose_name = 'Clue Type'
        verbose_name_plural = 'Clue Types'   

class StartingMessage(models.Model):
    message_text = models.TextField(max_length=1000)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE, related_query_name="adventure")
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, related_query_name="audio", blank=True, null=True)
    display = models.ForeignKey(MessageDisplay, on_delete=models.CASCADE, related_query_name="display")
    def __str__(self):
        return f'{self.adventure.name} - Starting Message'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['adventure'], name='message_adventure_constraint')
        ]
        verbose_name = 'Starting Message'
        verbose_name_plural = 'Starting Messages'

ClueOrder = models.IntegerChoices('ClueOrder', 'FIRST SECOND THIRD FOURTH FIFTH SIXTH SEVENTH EIGHTH NINTH TENTH ELEVENTH TWELFTH THIRTEENTH FOURTEENTH FIFTEENTH')

class Clue(models.Model):
    name = models.CharField(max_length=100)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE, related_query_name="adventure")
    answer = models.CharField(max_length=100)
    clueorder = models.IntegerField(choices=ClueOrder.choices)
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, related_query_name="audio", blank=True, null=True)
    display = models.ForeignKey(ClueDisplay, on_delete=models.CASCADE, related_query_name="display")
    def __str__(self):
        return f'{self.adventure.name} - Clue{self.clueorder}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['adventure', 'clueorder'], name='clue_adventure_constraint')
        ]


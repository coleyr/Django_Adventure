# Generated by Django 3.2.7 on 2021-09-24 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adventure', '0003_clue_character_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='clue',
            name='success_message',
            field=models.TextField(default='Enter message to be displayed on successful entry of answer', max_length=1000),
        ),
    ]

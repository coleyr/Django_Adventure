# Generated by Django 3.2.7 on 2021-09-28 19:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adventure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')])),
                ('description', models.TextField(max_length=500)),
                ('image', models.FileField(default='images/default.jpg', upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audiofile', models.FileField(upload_to='audio')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Clue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('character_name', models.CharField(default='Det. Ace Palmer', max_length=100)),
                ('message', models.TextField(default='Enter message here', max_length=1000)),
                ('success_message', models.TextField(default='Enter message to be displayed on successful entry of answer', max_length=1000)),
                ('answer', models.CharField(max_length=100)),
                ('clueorder', models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Fifth'), (6, 'Sixth'), (7, 'Seventh'), (8, 'Eighth'), (9, 'Ninth'), (10, 'Tenth'), (11, 'Eleventh'), (12, 'Twelfth'), (13, 'Thirteenth'), (14, 'Fourteenth'), (15, 'Fifteenth')])),
                ('adventure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='adventure', to='Adventure.adventure')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videofile', models.FileField(upload_to='video')),
                ('name', models.CharField(max_length=100)),
                ('clue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='clue', to='Adventure.clue')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagefile', models.FileField(upload_to='images')),
                ('name', models.CharField(max_length=100)),
                ('clue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='clue', to='Adventure.clue')),
            ],
        ),
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')])),
                ('hint_message', models.TextField(max_length=500)),
                ('audio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='audio', to='Adventure.audio')),
                ('clue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='clue', to='Adventure.clue')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='image', to='Adventure.image')),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='video', to='Adventure.video')),
            ],
        ),
        migrations.AddField(
            model_name='audio',
            name='clue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='clue', to='Adventure.clue'),
        ),
        migrations.AddConstraint(
            model_name='adventure',
            constraint=models.UniqueConstraint(fields=('name',), name='adventure_name_constraint'),
        ),
        migrations.AddConstraint(
            model_name='video',
            constraint=models.UniqueConstraint(fields=('videofile',), name='videofile_unique_constraint'),
        ),
        migrations.AddConstraint(
            model_name='image',
            constraint=models.UniqueConstraint(fields=('imagefile',), name='imagefile_unique_constraint'),
        ),
        migrations.AddConstraint(
            model_name='hint',
            constraint=models.UniqueConstraint(fields=('clue', 'name'), name='hint_name_constraint'),
        ),
        migrations.AddConstraint(
            model_name='clue',
            constraint=models.UniqueConstraint(fields=('adventure', 'clueorder'), name='clue_adventure_constraint'),
        ),
        migrations.AddConstraint(
            model_name='audio',
            constraint=models.UniqueConstraint(fields=('audiofile',), name='audiofile_unique_constraint'),
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-24 17:24

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
                ('message', models.TextField(default='Enter message here', max_length=1000)),
                ('answer', models.CharField(max_length=100)),
                ('clueorder', models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Fifth'), (6, 'Sixth'), (7, 'Seventh'), (8, 'Eighth'), (9, 'Ninth'), (10, 'Tenth'), (11, 'Eleventh'), (12, 'Twelfth'), (13, 'Thirteenth'), (14, 'Fourteenth'), (15, 'Fifteenth')])),
            ],
        ),
        migrations.CreateModel(
            name='ClueDisplay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Clue Type',
                'verbose_name_plural': 'Clue Types',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagefile', models.FileField(upload_to='images')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videofile', models.FileField(upload_to='video')),
                ('name', models.CharField(max_length=100)),
            ],
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
            model_name='cluedisplay',
            constraint=models.UniqueConstraint(fields=('name',), name='clue_type_constraint'),
        ),
        migrations.AddField(
            model_name='clue',
            name='adventure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='adventure', to='Adventure.adventure'),
        ),
        migrations.AddField(
            model_name='clue',
            name='audio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='audio', to='Adventure.audio'),
        ),
        migrations.AddField(
            model_name='clue',
            name='display',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='display', to='Adventure.cluedisplay'),
        ),
        migrations.AddField(
            model_name='clue',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='image', to='Adventure.image'),
        ),
        migrations.AddField(
            model_name='clue',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='video', to='Adventure.video'),
        ),
        migrations.AddConstraint(
            model_name='audio',
            constraint=models.UniqueConstraint(fields=('audiofile',), name='audiofile_unique_constraint'),
        ),
        migrations.AddField(
            model_name='adventure',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='image', to='Adventure.image'),
        ),
        migrations.AddConstraint(
            model_name='clue',
            constraint=models.UniqueConstraint(fields=('adventure', 'clueorder'), name='clue_adventure_constraint'),
        ),
        migrations.AddConstraint(
            model_name='adventure',
            constraint=models.UniqueConstraint(fields=('name',), name='adventure_name_constraint'),
        ),
    ]

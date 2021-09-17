# Generated by Django 3.2.7 on 2021-09-17 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adventure', '0005_alter_audio_audiofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='audio',
            name='audiofile',
            field=models.FileField(upload_to='static/media'),
        ),
    ]

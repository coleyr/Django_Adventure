# Generated by Django 3.2.7 on 2021-09-24 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adventure', '0002_auto_20210924_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='clue',
            name='character_name',
            field=models.CharField(default='Det. Ace Palmer', max_length=100),
        ),
    ]

# Generated by Django 3.1.2 on 2022-04-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adventure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='required',
            field=models.BooleanField(default=False),
        ),
    ]
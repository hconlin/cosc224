# Generated by Django 2.1.5 on 2019-04-25 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20190425_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepageevent',
            name='event_id',
            field=models.IntegerField(default=0),
        ),
    ]

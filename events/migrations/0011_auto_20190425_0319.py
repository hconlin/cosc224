# Generated by Django 2.1.7 on 2019-04-25 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20190425_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='age_requirement',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='homepageevent',
            name='age_requirement',
            field=models.IntegerField(),
        ),
    ]
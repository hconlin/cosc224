# Generated by Django 2.1.7 on 2019-02-16 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190216_2244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='user_id',
            new_name='author_id',
        ),
    ]

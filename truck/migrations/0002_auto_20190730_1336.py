# Generated by Django 2.1.8 on 2019-07-30 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='advance',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='less',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='trip_complete',
        ),
    ]

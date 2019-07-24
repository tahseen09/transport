# Generated by Django 2.2.2 on 2019-07-24 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0004_auto_20190724_2300'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='trip',
            unique_together={('truck', 'trip_start_date', 'sl_no')},
        ),
        migrations.RemoveField(
            model_name='trip',
            name='consignee',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='item',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='trip_complete',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='trip_end_time',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='trip_start_time',
        ),
    ]

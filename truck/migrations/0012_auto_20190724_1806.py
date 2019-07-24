# Generated by Django 2.2.2 on 2019-07-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0011_auto_20190701_1125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='weight',
            new_name='less',
        ),
        migrations.AddField(
            model_name='trip',
            name='diesel',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='mop',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='trip',
            name='rec_weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='shortage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='sl_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='status',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='trip',
            name='total_weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='tp_pass',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
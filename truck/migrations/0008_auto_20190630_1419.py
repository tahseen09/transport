# Generated by Django 2.2.2 on 2019-06-30 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0007_delete_truck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='expense',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]

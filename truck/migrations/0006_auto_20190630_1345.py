# Generated by Django 2.2.2 on 2019-06-30 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0005_auto_20190626_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='truck',
            field=models.CharField(max_length=40),
        ),
    ]

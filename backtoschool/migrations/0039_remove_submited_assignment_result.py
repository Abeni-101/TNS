# Generated by Django 3.0.8 on 2020-10-20 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backtoschool', '0038_auto_20201020_0611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submited_assignment',
            name='result',
        ),
    ]

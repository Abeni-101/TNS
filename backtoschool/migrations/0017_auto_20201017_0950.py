# Generated by Django 3.0.8 on 2020-10-17 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backtoschool', '0016_assignment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='subject',
            new_name='subject_name',
        ),
    ]

# Generated by Django 3.0.8 on 2020-10-08 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backtoschool', '0009_student_info_grade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_info',
            old_name='last_lastname',
            new_name='last_name',
        ),
    ]

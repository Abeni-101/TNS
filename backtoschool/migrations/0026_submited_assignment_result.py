# Generated by Django 3.0.8 on 2020-10-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backtoschool', '0025_submited_assignment_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='submited_assignment',
            name='result',
            field=models.IntegerField(null=True),
        ),
    ]
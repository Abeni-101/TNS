# Generated by Django 3.0.8 on 2020-10-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backtoschool', '0039_remove_submited_assignment_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='submited_assignment',
            name='result',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]

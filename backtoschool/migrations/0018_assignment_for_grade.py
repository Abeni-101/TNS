# Generated by Django 3.0.8 on 2020-10-17 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backtoschool', '0017_auto_20201017_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='for_grade',
            field=models.IntegerField(default=False),
        ),
    ]
# Generated by Django 3.0.8 on 2020-10-20 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backtoschool', '0030_auto_20201020_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submited_assignment',
            name='result',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]

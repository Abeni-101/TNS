# Generated by Django 3.0.8 on 2020-10-20 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backtoschool', '0041_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='first_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='last_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
# Generated by Django 3.0.8 on 2020-10-09 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backtoschool', '0010_auto_20201008_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_info',
            name='section',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]

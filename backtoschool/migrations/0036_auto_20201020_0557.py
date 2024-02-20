# Generated by Django 3.0.8 on 2020-10-20 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backtoschool', '0035_auto_20201020_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submited_assignment',
            name='first_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='submited_assignment',
            name='grade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='submited_assignment',
            name='last_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='submited_assignment',
            name='student_answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='submited_assignment',
            name='subject',
            field=models.CharField(blank=True, choices=[('Maths', 'Maths'), ('Chemistry', 'Chemistry'), ('Biology', 'Bilogy'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('English', 'English'), ('Civics', 'Civics'), ('ICT', 'ICT')], max_length=120, null=True),
        ),
    ]

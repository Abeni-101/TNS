# Generated by Django 3.0.8 on 2020-10-19 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backtoschool', '0026_submited_assignment_result'),
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
            field=models.IntegerField(default=False, null=True),
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
            field=models.CharField(blank=True, choices=[('Maths', 'Maths'), ('Chemistry', 'Chemistry'), ('Biology', 'Bilogy'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('English', 'English'), ('Civics', 'Civics'), ('ICT', 'ICT')], default=None, max_length=120, null=True),
        ),
    ]

# Generated by Django 3.0.8 on 2020-10-15 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backtoschool', '0014_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_info',
            name='branch',
            field=models.CharField(blank=True, choices=[('Natural_Scienc', 'Natural_Scienc'), ('Social_Scienc', 'Social_Scienc'), ('Not-student', 'Not-student')], max_length=50, null=True),
        ),
    ]

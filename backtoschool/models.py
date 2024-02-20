from django.db import models

from django.contrib.auth.models import User

class Student_info(models.Model):
	user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,)

	first_name=models.CharField(max_length=50,null=True,blank=True)

	last_name=models.CharField(max_length=50 , null=True,blank=True)

	branch_catagories=(("Natural_Scienc","Natural_Scienc"),("Social_Scienc","Social_Scienc"),("Not-student","Not-student"))

	branch=models.CharField(max_length=50,choices=branch_catagories, null=True,blank=True)

	gender_catagories=(("Male","Male"),("Female","Female"))

	gender=models.CharField(max_length=50,choices=gender_catagories, null=True,blank=True)

	Grade=models.IntegerField(null=True,blank=True)

	section=models.CharField(max_length=120,null=True,blank=True)

	profile_pic=models.ImageField(null=True,blank=True,default="images.jpg")

	def __str__(self):
		return self.first_name

class News(models.Model):
	title=models.CharField(max_length=120)
	content=models.TextField()
	published_date=models.DateTimeField(null=True,blank=True)

class Assignment(models.Model):
	teacher_name=models.CharField(max_length=50)
	subject_catagories=(("Maths","Maths"),
		                ("Chemistry","Chemistry"),
		                ("Biology","Bilogy"),
		                ("Chemistry","Chemistry"),
		                ("Physics","Physics"),
		                ("English","English"),
		                ("Civics","Civics"),
		                ("ICT","ICT"))
	subject_name=models.CharField(max_length=50,choices=subject_catagories)
	question=models.TextField()
	for_grade=models.IntegerField(default=False)
	catagories=(("Natural_Scienc","Natural_Scienc"),("Social_Scienc","Social_Scienc"))
	catagorie=models.CharField(max_length=50,choices=catagories , default=None)
	dead_line=models.CharField(max_length=50)

	def __str__(self):
		return self.subject_name
class Submited_Assignment(models.Model):
	first_name=models.CharField(max_length=120,null=True)
	last_name=models.CharField(max_length=120,null=True)
	subject_cat=(("Maths","Maths"),
	            ("Chemistry","Chemistry"),
	            ("Biology","Biology"),
	            ("Chemistry","Chemistry"),
	            ("Physics","Physics"),
	            ("English","English"),
	            ("Civics","Civics"),
	            ("ICT","ICT"))
	subject=models.CharField(max_length=120,choices=subject_cat,null=True)
	grade=models.IntegerField(null=True,)
	student_answer=models.TextField(null=True)
	result=models.IntegerField(default=None,blank=True,null=True)

	def __str__(self):
		return self.subject

    


# Create your models here.

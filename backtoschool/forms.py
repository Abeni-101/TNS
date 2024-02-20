from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student_info,News,Assignment,Submited_Assignment
from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
	class Meta:
		model=User
		fields=["username","email","password1","password2"]

'''class Student_Form(ModelForm):
	class Meta:
		model=Student_info

		fields='__all__'

		exclude=['user']'''
class Student_Form(ModelForm):
	class Meta:
		model=Student_info

		fields='__all__'

		exclude=["user"]
class News_Form(ModelForm):
	class Meta:
		model=News
		fields="__all__"

class Create_Assignment_Form(ModelForm):
	class Meta:
		model=Assignment

		fields="__all__"

class Submited_Assignments_Form(ModelForm):
	class Meta:
		model=Submited_Assignment
		fields='__all__'


from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.db.models import Q

from .forms import CreateUserForm,Student_Form,News_Form,Create_Assignment_Form,Submited_Assignments_Form

from .models import Student_info,News,Assignment,Submited_Assignment

from django.contrib.admin.views.decorators import staff_member_required



@unauthenticated_user
def registerpage(request):
	form=CreateUserForm()
	if request.method=="POST":
		form=CreateUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			username=form.cleaned_data.get("username")
			Student_info.objects.create(user=user,first_name=user.username)
			return redirect("/login")
	context={"form":form}
	return render(request,"backtoschool/register.html",context)
@unauthenticated_user
def loginpage(request):
	if request.method=="POST":
		username=request.POST.get("username")
		
		password=request.POST.get("password")

		user=authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect("/home")
		else:
		 messages.info(request,"The password or the username is incorrect !")

	return render(request,"backtoschool/login.html",{})
def logoutpage(request):
	logout(request)
	return redirect("/login")
@login_required(login_url='/login')
def home(request):
	student=Student_info.objects.all()
	boys=student.filter(gender="Male")
	girls=student.filter(gender="Female")
	Total_students=student.count()
	Total_boys=boys.count()
	Total_girls=girls.count()
	all_news=News.objects.all().order_by('-id')[:3]

	context={"Total_students":Total_students,
	         "Total_boys":Total_boys,
	         "Total_girls":Total_girls,
	          "all_news":all_news}

	return render(request,"backtoschool/home.html",context)

def search_student(request):
	if request.method=="POST":
		found=request.POST['srh']
		if found:
			match=Student_info.objects.filter(
				Q(first_name__icontains=found)|
				Q(last_name__icontains=found))
			if match:
				context={"match":match}
				return render(request,"backtoschool/search_result.html",context)
			else:
				return redirect("/home")
		else:
			return redirect("/home")
	return render(request,'backtoschool/search_result.html')

def account_settings(request):
	student=request.user.student_info
	
	form=Student_Form(instance=student)

	if request.method=="POST":
		form =Student_Form(request.POST,request.FILES,instance=student)
		if form.is_valid():
			form.save()
	context={"form":form,
	         }
	

	return render(request,"backtoschool/account_setting.html",context)

def more_info(request,pk):
	information=Student_info.objects.get(id=pk)
	context={"information":information}

	return render(request,"backtoschool/more_info.html",context)


@staff_member_required(login_url="/home")
def create_news(request):
	news=News_Form()
	if request.method=="POST":
		news=News_Form(request.POST)
		if news.is_valid():
			news.save()
			return redirect("/view_news")
	context={"news":news}
	return render(request,"backtoschool/news.html",context)
def view_news(request):
	all_news=News.objects.all().order_by('-id')
	context={"all_news":all_news}
	return render(request,"backtoschool/view_news.html",context)

def detail_news(request,pk):
	detail=News.objects.get(id=pk)
	context={"detail":detail}
	return render(request,"backtoschool/detail_page.html",context)

@staff_member_required(login_url="/home")
def create_assignment(request):
	assignment=Create_Assignment_Form()
	if request.method=="POST":
		assignment=Create_Assignment_Form(request.POST)
		if assignment.is_valid():
			assignment.save()
			return redirect("/view_assignment")
	context={"assignment":assignment}
	return render(request,"backtoschool/create_assignment.html",context)
def view_assignment(request):
	views_all=Assignment.objects.all()
	context={"views_all":views_all}
	return render(request,"backtoschool/view_assignment.html",context)
def submit_assignment(request,pk):
	view_all=Assignment.objects.get(id=pk)
	form=Submited_Assignments_Form()
	if request.method=="POST":
		form=Submited_Assignments_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/home")
	context={"view_all":view_all,
	         "form":form}
	return render(request,"backtoschool/submit_assignment.html",context)
@staff_member_required(login_url="/home")
def give_res(request):
	all_ass=Submited_Assignment.objects.all()
	context={"all_ass":all_ass}
	return render(request,"backtoschool/all_assignments.html",context)
@staff_member_required(login_url="/home")
def show_result(request,pk):
	result=Submited_Assignment.objects.get(id=pk)
	form=Submited_Assignments_Form(instance=result)
	if request.method=="POST":
		form=Submited_Assignments_Form(request.POST,instance=result)
		if form.is_valid():
			form.save()
	context={"result":result,"form":form}
	return render(request,"backtoschool/show_result.html",context)
def list_result(request):
	ls=Submited_Assignment.objects.all()
	context={"ls":ls}
	return render(request,"backtoschool/list_result.html",context)
def see_result(request,pk):
	see=Submited_Assignment.objects.get(id=pk)
	return render(request,"backtoschool/see_result.html",{"see":see})
@staff_member_required(login_url="/home")
def delete_ass(request,pk):
	obj=Assignment.objects.get(id=pk)
	if request.method=="POST":
		obj.delete()
		return redirect("/view_assignment")
    
	return render(request,"backtoschool/delete_assignment.html",{"obj":obj})





# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def signup(request):
	current_user = request.user.username
	obj = Student.objects.get(username=current_user)
	if obj :
		return redirect('/index')
	response = {}
	if request.method == 'POST' :
		#username=request.POST['username']
		regno = request.POST['regno']
		password = request.POST['password']
		rollno = request.POST['rollno']
		cgpa = request.POST['cgpa']
		branch = request.POST['branch']
		if User.objects.filter(username=regno):
			response['error']=1;
		else:
			User.objects.create_user(username = regno,password = password,email='')
			obj=Student()
			obj.username=regno
			br=Branch.objects.get(branch=branch)
			obj.regno=regno
			obj.password=password
			obj.rollno=rollno
			obj.cgpa=cgpa
			obj.branch=br
			obj.save()
	return render(request,'login.html',response)

def main(request):
	response={}
	try:
		current_user = request.user.username
		response['name']=current_user
		obj=Student.objects.get(regno= current_user)
		response['student']=obj
		response['file']=obj.resume
	except:
		return redirect('/signin')
	return render(request,'production/index.html',response)

def upcompany(request):
	response={}
	current_user = request.user.username
	response['name']=current_user
	std=Student.objects.get(username=current_user)
	obj=Company.objects.filter(min_cgpa__lte=std.cgpa)
	response['company']=obj
	return render(request,'production/upcompany.html',response)

def addCompany(request):
	response = {}
	current_user = request.user.username
	if request.method == "POST":
		company = Company()
		name = request.POST["name"]
		if Company.objects.filter(name=name):
			return redirect("/")
		company.name = name
		company.description = request.POST["description"]
		company.min_cgpa = request.POST["min_cgpa"]
		obj=Student.objects.get(username=current_user)
		company.coordinator = obj
		company.save()
		if request.POST.get("CSE") :
			branch = Branch.objects.get(branch="CSE")
			company.branchOptions.add(branch)
		if request.POST.get("ECE") :
			branch = Branch.objects.get(branch="ECE")
			company.branchOptions.add(branch)
		if request.POST.get("EEE") :
			branch = Branch.objects.get(branch="EEE")
			company.branchOptions.add(branch)
		if request.POST.get("MME") :
			branch = Branch.objects.get(branch="MME")
			company.branchOptions.add(branch)
		if request.POST.get("BIO") :
			branch = Branch.objects.get(branch="BIO")
			company.branchOptions.add(branch)
		company.save()
	return render(request, 'addCompany.html', response)


def addCompany(request):
	response={}
	return render(request,'addCompany.html',response)

def signin(request):
	current_user = request.user.username
	obj = Student.objects.get(username=current_user)
	if obj :
		return redirect('/index')
	response = {}
	if request.method == 'POST' :
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is None :
			return render(request,'login.html',response)
		else :
			login(request,user)
			return redirect('/index')
	return render(request,'login.html',response)


def home(request):
	return HttpResponse("<h1>Welcome</h1><title>Home</title>")

def acceptcomp(request,compname):

	obj=Company.objects.get(name=compname)
	response={}
	response['company']=obj
	current_user=request.user.username
	response['name']=current_user
	std=Student.objects.get(username=current_user)
	if Application.objects.filter(company=obj,student=std).exists():
		response['flag']=1
		response['company']=Company.objects.filter(min_cgpa__lte=std.cgpa)
		return render(request,'production/upcompany.html',response)
	return render(request,'production/acceptcomp.html',response)


def logout_view(request):
    logout(request.user)
    return render(request,'login.html')		

def applycomp(request,req):
	if request.method == 'POST' :	
		obj=Application()
		current_user = request.user.username
		std = Student.objects.get(username=current_user)
		obj.student=std
		obj.company=Company.objects.get(name=req)
		file=request.FILES.get('resume')
		obj.attachment=file
		obj.file_name=file.name
		obj.status=1
		obj.save()
		return render(request,'production/index.html')
	return render(request,'production/index.html')


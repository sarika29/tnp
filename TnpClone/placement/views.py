# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *

# Create your views here.


def signup(request):
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

def profile(request):
	response = {}
	regno = 811734
	student = Student.objects.get(regno=regno)
	response['student'] = student

	return render(request, 'profile.html', response)

def main(request):

	response={}
	current_user = request.user.username
	response['name']=current_user
<<<<<<< HEAD


	obj=Student.objects.get(regno= 123)

=======
	obj=Student.objects.get(regno= current_user)
>>>>>>> da313927c6265a5c1ef1743058dac826a14d854f
	response['student']=obj
	response['file']=obj.resume
	return render(request,'production/index.html',response)

def upcompany(request):
	response={}
	current_user = request.user.username
	response['name']=current_user
	std=Student.objects.get(username=current_user)
	obj=Company.objects.filter(min_cgpa__lte=std.cgpa)
	response['company']=obj
	return render(request,'production/upcompany.html',response)

<<<<<<< HEAD
def addCompany(request):
	response={}
	return render(request,'addCompany.html',response)
=======
def signin(request):
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

>>>>>>> da313927c6265a5c1ef1743058dac826a14d854f


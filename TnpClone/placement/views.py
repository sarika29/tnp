# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
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
	obj=Student.objects.get(regno= 123)
	response['student']=obj
	response['file']=obj.resume
	return render(request,'production/index.html',response)

def upcompany(request):
	response={}
	current_user = request.user.username
	response['name']=current_user
	return render(request,'production/upcompany.html',response)

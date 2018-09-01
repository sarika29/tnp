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
	print(student.branch)
	company = Company.objects.filter(min_cgpa=student.cgpa)
	print(company)
	response['student'] = student
	response['company'] = company

	return render(request, 'profile.html', response)

def addCompany(request):
	response = {}
	if request.method == "POST":
		company = Company()
		company.name = request.POST["name"]
		company.description = request.POST["description"]
		company.min_cgpa = request.POST["min_cgpa"]
		company.save()

	return render(request, 'addCompany.html', response)



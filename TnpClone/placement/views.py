# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
<<<<<<< HEAD
from django.contrib.auth.models import User
=======
from .models import *
>>>>>>> 31c4604744205ac0caf2eeb5d7ed15073d5c135c

# Create your views here.


def signup(request):
	response = {}
	if request.method == 'POST' :
		regno = request.POST['regno']
		password = request.POST['password']
<<<<<<< HEAD
		rollno = request.POST['rollno']
		cgpa = request.POST['cgpa']
		branch = request.POST['password']
		if User.objects.filter(username=username):
			response['error']=1;
		else:
			User.objects.create_user(username = regno,password = password,email='')
	return render(request,'login.html',response)
=======
		user = authenticate(username=username, password=password)
		if user is None :
			return render(request,'login.html',response)
		else :
			login(request,user)
			return redirect('/index')
	return render(request,'login.html',response)


<<<<<<< HEAD


=======
def profile(request):
	response = {}
	regno = 811734
	student = Student.objects.get(regno=regno)
	response['student'] = student

	return render(request, 'profile.html', response)

>>>>>>> 31c4604744205ac0caf2eeb5d7ed15073d5c135c
>>>>>>> 7194dbae6ad25df7de985907c05fdb8080b88b67

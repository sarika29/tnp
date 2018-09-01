# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .models import *

# Create your views here.


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


def profile(request):
	response = {}
	regno = 811734
	student = Student.objects.get(regno=regno)
	response['student'] = student

	return render(request, 'profile.html', response)


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def signup(request):
	response = {}
	if request.method == 'POST' :
		regno = request.POST['regno']
		password = request.POST['password']
		rollno = request.POST['rollno']
		cgpa = request.POST['cgpa']
		branch = request.POST['password']
		if User.objects.filter(username=username):
			response['error']=1;
		else:
			User.objects.create_user(username = regno,password = password,email='')
	return render(request,'login.html',response)
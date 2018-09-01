# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def signup(request):
	response = {}
	if request.method == 'POST' :
		username = request.POST['regno']
		password = request.POST['password']
		
		User.objects.create_user(username = username,password = password,email='')
	return render(request,'login.html',response)
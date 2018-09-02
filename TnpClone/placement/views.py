# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
import xlwt
from xlwt import Workbook,easyxf,Formula
from django.contrib.auth.decorators import login_required,user_passes_test
import requests
# Create your views here.

def checkuserifsuperuser(user):
    if user.is_superuser:
        return True
    else:
        return False

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

@login_required(login_url='/signin')
def main(request):
	response={}
	current_user = request.user.username
	response['name']=current_user

	obj=Student.objects.get(regno= current_user)

	response['student']=obj
	response['file']=obj.resume
	return render(request,'production/index.html',response)

@login_required(login_url='/signin')
def upcompany(request):
	response={}
	current_user = request.user.username
	response['name']=current_user

	std=Student.objects.get(regno=current_user)
	obj=Company.objects.filter(min_cgpa__lte=std.cgpa)
	response['company']=obj
	response['student']=std
	print response['student']
	return render(request,'production/upcompany.html',response)

@login_required(login_url='/signin')
@user_passes_test(checkuserifsuperuser, login_url='/signin')
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


def home(request):
	return HttpResponse("<h1>Welcome</h1><title>Home</title>")

@login_required(login_url='/signin')
def acceptcomp(request,compname):
	obj=Company.objects.get(name=compname)
	response={}
	response['company']=obj
	current_user=request.user.username
	response['name']=current_user
	std=Student.objects.get(regno=current_user)
	response['student']=std
	if Application.objects.filter(company=obj,student=std).exists():
		response['flag']=1
		response['company']=Company.objects.filter(min_cgpa__lte=std.cgpa)
		return render(request,'production/upcompany.html',response)
	return render(request,'production/acceptcomp.html',response)

@login_required(login_url='/signin')
def logout_view(request):
	logout(request)
	return redirect('/signin')

@login_required(login_url='signin/')
def applycomp(request,req):
	if request.method == 'POST' :	
		obj=Application()
		current_user=request.user.username
		std=Student.objects.get(regno=current_user)
		obj.student=std
		obj.company=Company.objects.get(name=req)
		file=request.FILES.get('resume')
		obj.attachment=file
		obj.file_name=file.name
		obj.status=1
		obj.save()
		return redirect('/index')
	return render(request,'production/index.html')
 
@login_required(login_url='signin/')
def status(request, compname):
	response = {}
	current_user = request.user.username
	std = Student.objects.get(username=current_user)
	obj = Company.objects.get(name=compname)
	status = Application.objects.get(student=std, company=obj)
	print(status)
	if status :
		status = status.status
		response["status"] = status
	return render(request, 'production/status.html', response)

@login_required(login_url='signin/')
def listcomp(request):
	response={}
	current_user=request.user.username
	response['name']=current_user
	std=Student.objects.get(regno=current_user)
	if std.iscoordinator:
		obj=Company.objects.filter(coordinator=std)
		response['company']=obj
		response['student']=std
		return render(request,'production/listcomp.html',response)
	return redirect('/index')

@login_required(login_url='signin/')
def liststd(request,compname):
	response={}
	current_user=request.user.username
	response['name']=current_user
	response['company']=compname
	comp=Company.objects.get(name=compname)
	obj=Student.objects.get(username=current_user)
	if comp.coordinator != obj:
		return redirect('/index')
	std1=Application.objects.filter(company=comp)
	response['student']=std1
	return render(request,'production/liststd.html',response)

@login_required(login_url='signin/')
def export_users_xls(request,compname):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="studentlist.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Student List')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Registration Number', 'Roll Number', 'CGPA', 'Branch','Resume', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    comp=Company.objects.filter(name=compname)
    rows = Application.objects.filter(company=comp)

    for row in rows:
    	std=row.student
    	br=std.branch
    	#std2=Student.objects.get(regno=std.regno).values_list('regno', 'rollno', 'cgpa', 'branch','resume')
        row_num += 1
        ws.write(row_num, 0, std.regno, font_style)
        ws.write(row_num, 1, std.rollno, font_style)
        ws.write(row_num,2, std.cgpa, font_style)

        ws.write(row_num,3, br.branch, font_style)
        check="http://127.0.0.1:8000/resume"+str(row.attachment.url)
        print check
        ws.write(row_num,4, check, font_style)

    	wb.save(response)
    return redirect('/index')

@login_required(login_url='signin/')
def shortlist(request):
  	return render(request,'production/shortlistupload.html',response)

@login_required(login_url='signin/')
def upload_shortlist(request,compname):
	loc = ("path of file")

	# To open Workbook
	wb = xlrd.open_workbook(loc)
	sheet = wb.sheet_by_index(0)
	 
	# For row 0 and column 0
	sheet.cell_value(0, 0)

	return redirect('/index')

# def send_info(request):
# 	if request.method == "POST" :
# 		info = SendInfo()
# 		info.name = request.POST["name"]
# 		info.ctc = request.POST["ctc"]
# 		info.description = request.POST["description"]
# 		info.save()
# 		msg = 'Company:' + info.name + '\nCTC:' + info.ctc + '\nComment:' + info.description
# 		access_token = 'EAADfd1ZAZAWckBAHAjfGaSCT20sf95eqBeyVrbj9oA3CrUYdSuikPyDhenw9RTUEDjmtyFyn6C5EHgAjaxHjlYfohukza5WtmVmd8Gairg3D7Kvh8BIJyCfMNAANilsJhX4tI6rPzXhbifhYb63d6ZArX2yZADoG518B60p20gZDZD'
# 		access_token = 'access_token=' + access_token   

# 		message = 'message=' + msg

# 		link = 'https://graph.facebook.com/v3.1/me/feed?' + message + '&' + access_token

# 		# response = requests.post(link)
# 		# response.raise_for_status()

# 	return render(request, 'fb.html')

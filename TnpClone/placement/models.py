# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def get_resume_path(instance, filename):
	return 'resume/{0}/{1}'.format(instance.regno, filename)

def make_resume_path(instance, filename):
	return 'resume/{0}/{1}'.format(instance.company.name, instance.student.username)


class Branch(models.Model):
	branch_choice = (
			('CSE','CSE'),
			('ECE','ECE'),
			('EEE','EEE'),
			('MME','MME'),
			('BIO','BIO'),
		)
	branch = models.CharField(max_length=10, choices=branch_choice, default='CSE')

	def __str__(self):
		return self.branch

class Student(models.Model):
	username = models.CharField(max_length=255)
	regno = models.IntegerField(unique=True)
	rollno = models.IntegerField(unique=True)
	cgpa = models.FloatField()
	branch=models.ForeignKey(Branch, on_delete=models.CASCADE)
	resume = models.FileField(upload_to=get_resume_path, blank=True, null=True)
	iscoordinator = models.BooleanField(default=False)

	def __str__(self):
		return self.username

class Company(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	min_cgpa = models.FloatField()
	branchOptions = models.ManyToManyField(Branch, related_name='company', blank=True)
	coordinator = models.ForeignKey(Student, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Application(models.Model):
	student= models.ForeignKey(Student, on_delete=models.CASCADE)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	status_choices = (
			(1, 'submitted'),
			(2, 'onlineTest'),
			(3, 'interview'),
			(4, 'selected'),
		)
	status = models.IntegerField(choices=status_choices, default=1)
	file_name = models.CharField(max_length=100,default="xxx")
	attachment = models.FileField(upload_to=make_resume_path, unique=True)

	def __str__(self):
		return self.student.username + str(self.status)

class SendInfo(models.Model):
    name = models.CharField(max_length=255)
    ctc = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return self.name
        

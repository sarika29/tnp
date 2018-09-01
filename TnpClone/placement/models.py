# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Branches(models.Model):
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


class CompanyInfo(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	min_cgpa = models.IntegerField()
	branchOptions = models.ManyToManyField(Branches, related_name='company', blank=True)

	def __str__(self):
		return self.name



class User(models.Model):
	username = models.CharField(max_length=255)
	regno = models.IntegerField(unique=True)
	rollno = models.IntegerField(unique=True)
	cgpa = models.IntegerField()
	resume = models.FileField()

	def __str__(self):
		return self.username

class Application(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
	status_choices = (
			(1, 'submitted'),
			(2, 'onlineTest'),
			(3, 'selected'),
		)
	status = models.IntegerField(choices=status_choices, default=1)

	def __str__(self):
		return self.user.username + str(self.status)

		
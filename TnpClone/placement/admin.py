# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Branch)
admin.site.register(Company)
admin.site.register(Student)
admin.site.register(Application)
admin.site.register(SendInfo)


from django.contrib import admin
from . models import *
# Register your models here.

class addNewStudent(admin.ModelAdmin):
    list_display =('id','name','email','password')
admin.site.register(add_new_student,addNewStudent)

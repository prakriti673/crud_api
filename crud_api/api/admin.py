from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    # data will be shown in the following format with these fields
    list_display=['id','name','roll','city']

admin.site.register(Student,StudentAdmin)
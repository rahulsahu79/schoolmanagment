from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display=('id','name')
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display=('id','name')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display =('teacher_id','name','gender','date_of_birth','mobile','joining_date','qualification','exprience','address','city','state','zip_code','country')
    list_filter=('gender','city','state')
    search_fields=('teacher_id','joining_date')


    
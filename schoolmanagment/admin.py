from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    search_fields = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    list_filter = ('father_name', 'mother_name')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'gender', 'date_of_birth', 'student_class', 'joining_date', 'mobile_number', 'admission_number', 'section')
    search_fields = ('first_name', 'last_name', 'student_id', 'student_class', 'admission_number')
    list_filter = ('gender', 'student_class', 'section')
    readonly_fields = ('student_image',)  # Optional: makes the image field read-only

# for teacher section 
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
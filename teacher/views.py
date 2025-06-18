from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.contrib import messages

# Create your views here.

def add_teacher(request):
    if request.method == "POST":
        try:
            teacher_id = request.POST['teacher_id']
            name = request.POST['name']
            gender = request.POST['gender']
            date_of_birth = request.POST['date_of_birth']
            mobile = request.POST['mobile']
            joining_date = request.POST['joining_date']
            qualification = request.POST['qualification']
            exprience = request.POST['exprience']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['city']
            zip_code = request.POST['zip_code']
            country  = request.POST['country']
        
            teacher = Teacher(teacher_id = teacher_id, name = name , gender = gender , date_of_birth = date_of_birth , mobile = mobile , joining_date = joining_date, qualification = qualification, exprience = exprience,address = address , city = city ,state=state, zip_code = zip_code,country = country)
            print(request.POST)
            teacher.save()
            messages.success(request,"new record added ")
            return redirect('teacher_list')
        except Exception as e :
            messages.error(request,f"error {e} ")
        
        
    return render(request,"teachers/add-teacher.html")

def teacher_list(request):
    teacher_list = Teacher.objects.all()
    context = {
        'teacher_list' : teacher_list
    }
    return render(request,"teachers/teachers.html",context)

def edit_teacher(request,teacher_id):
    teacher_edit = get_object_or_404(Teacher,teacher_id = teacher_id)
    if request.method == "POST":
        
        try:
             
            teacher_edit.name = request.POST['name']
            teacher_edit.gender = request.POST['gender']
            teacher_edit.date_of_birth = request.POST['date_of_birth']
            teacher_edit.mobile = request.POST['mobile']
            teacher_edit.joining_date = request.POST['joining_date']
            teacher_edit.qualification = request.POST['qualification']
            teacher_edit.exprience = request.POST['exprience']
            teacher_edit.address = request.POST['address']
            teacher_edit.city = request.POST['city']
            teacher_edit.state = request.POST['state']
            teacher_edit.zip_code = request.POST['zip_code']
            teacher_edit.country  = request.POST['country']
        
            #teacher = Teacher( name = name , gender = gender , date_of_birth = date_of_birth , mobile = mobile , joining_date = joining_date, qualification = qualification, exprience = exprience,address = address , city = city , zip_code = zip_code,country = country)
            teacher_edit.save()
            messages.success(request,"data edit successfully ")
            return redirect('teacher_list')
        
        except Exception as e :
            print(f"Error while saving teacher: {e}")
            messages.error(request,f"error {e} ")
            
    return render(request,"teachers/edit-teacher.html",{'teacher_edit':teacher_edit})
        
    
def delete_teacher(request,teacher_id):
    teacher = get_object_or_404(Teacher,teacher_id=teacher_id)
    teacher.delete()
    return redirect('teacher_list')

def view_teacher(request,teacher_id):
    teacher = get_object_or_404(Teacher,teacher_id=teacher_id)
    context = {'teacher':teacher}
    return render(request,"teachers/teacher-details.html",context)

def assign_teacher(request):
    if request.method == "POST":
        teacher_id = request.POST.get("teacher_id")
        grade_id = request.POST.get("grade_id")
        section_id = request.POST.get("section_id")
        
        try:
        
            teacher = get_object_or_404(Teacher, id = teacher_id)
            grade = get_object_or_404(Grade, id = grade_id)
            section = get_object_or_404(Section, id = section_id)
            
            print("Form Data:", request.POST)

            teacher.grades = grade
            teacher.sections = section
            teacher.save()
            print("Form Data:", request.POST)

            print("Teacher ID from POST:", teacher_id)

            messages.success(request, "Teacher assigned to Grade and Section successfully!")
            return redirect('teacher_list') 
        
        except (Teacher.DoesNotExist, Grade.DoesNotExist, Section.DoesNotExist):
            messages.error(request, "Invalid data selected.")
        
    teachers = Teacher.objects.all()
    grades = Grade.objects.all()
    sections = Section.objects.all()
    context={
        'teachers':teachers,
        'grades' : grades,
        'sections' : sections
    }
    return render(request, "teachers/assign_teachr.html",context)
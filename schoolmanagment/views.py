from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseForbidden
from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib import messages
from django.utils.text import slugify

# Create your views here.

# starting point
  
def add_student(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        date_of_birth_str = request.POST.get('date_of_birth')
        try:

            date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d').date()
        except ValueError:

            messages.error(request, "Invalid date format. Use YYYY-MM-DD.")
            return redirect('add_student')
        student_class = request.POST.get('student_class')
        religion = request.POST.get('religion')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        section = request.POST.get('section')
        student_image = request.FILES.get('student_image')

        # Retrieve parent data from the form
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        father_email = request.POST.get('father_email')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        mother_mobile = request.POST.get('mother_mobile')
        mother_email = request.POST.get('mother_email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')

        # save parent information
        parent = Parent.objects.create(
            father_name= father_name,
            father_occupation= father_occupation,
            father_mobile= father_mobile,
            father_email= father_email,
            mother_name= mother_name,
            mother_occupation= mother_occupation,
            mother_mobile= mother_mobile,
            mother_email= mother_email,
            present_address= present_address,
            permanent_address= permanent_address
        )

        # Save student information
        student = Student.objects.create(
            first_name= first_name,
            last_name= last_name,
            student_id= student_id,
            gender= gender,
            date_of_birth= date_of_birth,
            student_class= student_class,
            religion= religion,
            joining_date= joining_date,
            mobile_number = mobile_number,
            admission_number = admission_number,
            section = section,
            student_image = student_image,
            parent = parent
        )
        #create_notification(request.user, f"Added Student: {student.first_name} {student.last_name}")
        messages.success(request, "Student added Successfully")

        return redirect('student_list') 

  

    return render(request,"students/add-student.html")





def student_list(request):
    student_list = Student.objects.select_related('parent').all()
    context = {
        'student_list' : student_list
    }

    return render(request,"students/students.html" ,context)


def edit_student(request,slug):
     student = get_object_or_404(Student,slug=slug)
     parent = student.parent if hasattr(student,'parent') else None
     if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        date_of_birth_str = request.POST.get('date_of_birth')
        try:

            date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d').date()
        except ValueError:

            messages.error(request, "Invalid date format. Use YYYY-MM-DD.")
            return redirect('add_student', slug=slug)
        student_class = request.POST.get('student_class')
        religion = request.POST.get('religion')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        section = request.POST.get('section')
        student_image = request.FILES.get('student_image')

        # Retrieve parent data from the form
        parent.father_name = request.POST.get('father_name')
        parent.father_occupation = request.POST.get('father_occupation')
        parent.father_mobile = request.POST.get('father_mobile')
        parent.father_email = request.POST.get('father_email')
        parent.mother_name = request.POST.get('mother_name')
        parent.mother_occupation = request.POST.get('mother_occupation')
        parent.mother_mobile = request.POST.get('mother_mobile')
        parent.mother_email = request.POST.get('mother_email')
        parent.present_address = request.POST.get('present_address')
        parent.permanent_address = request.POST.get('permanent_address')
        parent.save()

        
        # Save student information
    
        student.first_name= first_name
        student.last_name= last_name
        student.student_id= student_id
        student.gender= gender
        student.date_of_birth= date_of_birth
        student.student_class= student_class
        student.religion= religion
        student.joining_date= joining_date
        student.mobile_number = mobile_number
        student.admission_number = admission_number
        student.section = section
        student.student_image = student_image
        student.save()

        #create_notification(request.user, f"Added Student: {student.first_name} {student.last_name}")
        messages.success(request, "Student added Successfully")

        return redirect('student_list') 

     return render(request,"students/edit-student.html",{'student':student, 'parent' : parent})


def view_student(request,slug):
    student = get_object_or_404(Student,slug = slug)
    context = {
        'student' : student
    }
    return render(request,'students/student-details.html',context)

def delete_student(request,slug):
    if request.method == "POST":
        student = get_object_or_404(Student,slug=slug)
        student_name = f"{student.first_name} {student.last_name} "
        student.delete()

        return redirect('student_list')
    return HttpResponseForbidden()


# teacter section 


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
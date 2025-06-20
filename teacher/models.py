from django.db import models

# Create your models here.

class Grade(models.Model):
    name = models.CharField(max_length=5,null=True,blank=True)
    
class Section(models.Model):
    name = models.CharField(max_length=5)
    grades = models.ForeignKey(Grade,on_delete=models.CASCADE,null=True,blank=True)

class Teacher(models.Model):
    
    teacher_id = models.CharField(max_length=200,unique=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10,choices=[("Male","male"),("Female","Female"),("Others","Others")])
    date_of_birth = models.DateField()
    mobile = models.CharField(max_length=15)
    joining_date = models.DateField()
    qualification = models.CharField(max_length=100)
    exprience = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.PositiveIntegerField()
    country = models.CharField(max_length=100)
    grades = models.ForeignKey(Grade,on_delete=models.CASCADE,null=True,blank=True)
    sections = models.ForeignKey(Section,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return f"{self.teacher_id or 'N/A'} {self.name}"

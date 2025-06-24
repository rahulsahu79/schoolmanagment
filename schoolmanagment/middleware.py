from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseForbidden
class RoleAccessMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self,request):
        path = request.path
        print("middleware runing ",path)
        if path.startswith('/schoolmanagment/teacher/'):
            if not request.user.is_authenticated:
                print("redirect to teacher login ", )
                return redirect(reverse('login'))
            
            if not getattr(request.user,'is_teacher',False):
                return HttpResponseForbidden(" teacher only ")
            
        # for student 
        if path.startswith('/schoolmanagment/student/'):
            if not request.user.is_authenticated:
                return redirect(reverse('login'))
            if not getattr(request.user,'is_student',False):
                return HttpResponseForbidden('student only ')
            
        return self.get_response(request)
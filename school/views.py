from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return render(request,"authentication/login.html")

def dashboard(request):
    return render(request,"students/student-dashboard.html")
    
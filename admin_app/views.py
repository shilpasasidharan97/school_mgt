from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')

def admin_home(request):
    return render(request,'admin_home.html')

def student_details(request):
    return render(request,'studentdetails.html')

def teacher_details(request):
    return render(request,'teacherdetails.html')

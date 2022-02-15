from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')

def admin_home(request):
    return render(request,'admin_home.html')

def studentdetails(request):
    return render(request,'studentdetails.html')
def addstudent(request):
    return render(request,'addstudent.html')
def staffdetails(request):
    return render(request,'staffdetails.html')
def addstaff(request):
    return render(request,'addstaff.html')


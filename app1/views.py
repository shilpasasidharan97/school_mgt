from django.shortcuts import render

# Create your views here.
def  index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def admission(request):
    return render(request,'admission.html')
def gallery(request):
    return render(request,'gallery.html')


def erp_login(request):
    return render(request,'erp-login.html')
def signup(request):
    return render(request,'signup.html')

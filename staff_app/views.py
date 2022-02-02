from django.shortcuts import render

# Create your views here.
def staffhome(request):
    return render(request,'staffhome.html')
def staffprofile(request):
    return render(request,'staffprofile.html')
def staffattandance(request):
    return render(request,'staffattandance.html')
def studentlist(request):
    return render(request,'studentlist.html')
def studentattandance(request):
    return render(request,'studentattandance.html')
from django.urls import path
from django.urls.conf import include
from . import views

app_name='admin_app'

urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    path('adminhome',views.admin_home,name='adminhome'),
    path('studentdetails',views.studentdetails,name='student'),
    path('addstudent',views.addstudent,name='newstudent'),
    path('staff',views.staffdetails,name='staff'),
    path('newstaff',views.addstaff,name='newstaff'),
    
]
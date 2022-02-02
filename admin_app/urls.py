from django.urls import path
from django.urls.conf import include
from . import views

app_name='admin_app'

urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    path('adminhome',views.admin_home,name='adminhome'),
    path('studentdetails',views.student_details,name='student_details'),
    path('staffdetails',views.teacher_details,name='teacher_details')
]
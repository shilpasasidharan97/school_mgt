from tkinter import N
from django.urls import path
from django.urls.conf import include
from . import views

app_name='staff_app'

urlpatterns = [
    path('staffhome',views.staffhome,name='staffhome'),
    path('staffprofile',views.staffprofile,name='staffprofile'),
    path('staffattandance',views.staffattandance,name='staffattandance'),
    path('studentlist',views.studentlist,name='studentlist'),
    path('studentattandance',views.studentattandance,name='studentattandance')
]
from django.urls import path
from django.urls.conf import include
from . import views

app_name='student_app'

urlpatterns = [
    path('myprofile',views.myprofile,name='studentprofile')
]
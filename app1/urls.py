from django.urls import path
from django.urls.conf import include
from . import views

app_name='app1'

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.erp_login,name='login'),
    path('about',views.about,name='about'),
    path('admission',views.admission,name='admission'),
    path('gallery',views.gallery,name='gallery'),
    path('signup',views.signup,name='signup')
]
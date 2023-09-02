
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.userlogin,name='userlogin'),
    path('register/',views.registeruser,name='registeruser'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('form/',views.form,name='form')
]

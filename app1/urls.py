

from django.urls import path
from . import views


urlpatterns = [
    
    path('login', views.login, name='login'),
    path('',views.register, name='register'),
    path('read',views.read,name='read'),
    path('forgot-password',views.forgot_pass,name='forgot-password'),
    path('index',views.index,name='index')

]
# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resume_1/', views.resume_1, name='resume_1'),
    path('resume_2/', views.resume_2, name='resume_2'),
    path('resume_template/', views.resume_template, name='resume_template'),
]
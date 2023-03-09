from django.urls import path
from . import views

urlpatterns = [
    path('',views.job_list,name='job_list'),
    path('job_details/<str:pk>',views.job_details,name='Job_details'),
]
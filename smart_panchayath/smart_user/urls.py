from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('index/', views.Index, name='index'),
    path('home/', views.Home, name='Home'),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('features/', views.Features, name='features'),
    path('services/', views.Services, name='services'),
    path('user_registration/', views.User_Registration, name='User_Registration'),
    path('User_Login/', views.User_Login, name='User_Login'),
    path('Muncipality_Login/', views.Muncipality_Login, name='Muncipality_Login'),
    path('Corporation_Login/', views.Corporation_Login, name='Corporation_Login'),
    path('panchayath_login/', views.Panchayath_Login, name='Panchayath_Login'),
    path('category/', views.category, name='category'),
    path('error/', views.error, name='error'),
    path('Panchayath_List/', views.Panchayath_list, name='Panchayath_List'),
    path('Muncipality_List/', views.Muncipality_list, name='Muncipality_List'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('job-detail/', views.job_detail, name='job-detail'),
    path('job-list/', views.job_list, name='job-list'),

]

from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('new-page/', views.new_page, name='new_page'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    
    
    
    # Define the index URL
    # Add other app-specific URLs as needed
]
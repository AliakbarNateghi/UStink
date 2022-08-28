from django.contrib import admin
from django.urls import path
from ustink import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_view, name="login"),
    path('register/', views.RegisterPage.as_view(), name="register"),
    path('contactus/', views.contactus, name="contactus"),
    path('edit/', views.edit, name="edit"),
]

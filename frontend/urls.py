from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from ustink import views

urlpatterns = [
    path('', views.home, name="home"),
    path('', views.index, name='index'),
    path('login/', views.LoginView, name="login"),
    path('register/', views.RegisterPage.as_view(), name="register"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('contactus/', views.contactus, name="contactus"),
    path('edit/', views.edit, name="edit"),
    path('completeProfile/', views.completeProfile, name="completeProfile"),

]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.LogIn, name='blog-home'),
    path('register/', views.SignUp, name='blog-register'),
]
from django.urls import path
from users_app import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.contrib.auth import authenticate

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LoginView.as_view(template_name='logout.html'), name='logout'),
]

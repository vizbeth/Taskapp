from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.htm'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.htm'), name='logout')
]

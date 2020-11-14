from django.urls import path
from . import views

urlpatterns = [
    path('Cadastro/', views.Cadastro, name='Cadastro'),
    path('Login/', views.Login, name='Login'),
    path('logout', views.logout, name='logout'),
]
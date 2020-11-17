from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Sobre', views.Sobre, name='Sobre'),
    path('Contato', views.Contato, name='Contato'),
]
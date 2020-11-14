from django.urls import path
from . import views

urlpatterns = [
    path('Garagem/', views.garagem, name='garagem'),
    path('CriarVaga/', views.CriarVaga, name='CriarVaga'),
    path('<int:valor>', views.comprarvaga, name='comprarvaga'),
]
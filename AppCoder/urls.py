from AppCoder import views
from django.urls import path

urlpatterns = [
    path('inicio/', views.inicio ),
    path('curso/', views.curso ),
    path('profesores/', views.profesor  ),
    path('estudiantes/', views.estudiantes ),
    path('entregables/', views.entregables),

]
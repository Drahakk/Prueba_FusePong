from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('logout/', views.exit, name='exit'),
    path('register/', views.register, name='register'),
    path('proyectoscreados/', views.crear, name='crear'),
    path('proyectoscreados/editar/<int:id>', views.editar, name='editar'),
    path('proyectoscreados/', views.form, name='form'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),

    path('tickets/', views.tickets, name='tickets'),
    path('ticket/', views.creart, name='creart'),
    path('ticket/editart/<int:Id>', views.editart, name='editart'),
    path('ticket/', views.formt, name='formt'),
    path('eliminart/<int:Id>', views.eliminart, name='eliminart'),

]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
	path('crearUsuario/',views.crearUsuario,name='crearUsuario'),
    path('ingresar/',views.ingresar,name='ingresar'),
]
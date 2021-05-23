from django.shortcuts import render,redirect

# Create your views here.
def home(request):
	context = {}
	return render(request, 'trabajaYa/home.html',context)

def crearUsuario(request):
	context = {}
	return render(request, 'trabajaYa/registrarse.html',context)

def ingresar(request):
	context = {}
	return render(request, 'trabajaYa/login.html',context)
from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def store(request):
 products = Product.objects.all()
 context = {'products':products}
 return render(request, 'store/store.html', context)

def cart(request):
 context = {}
 return render(request, 'store/cart.html', context)

def checkout(request):
 context = {}
 return render(request, 'store/checkout.html', context)


def login(request):
    return render(request, 'store/login.html')

def respuesta(request):
    EmailX = request.GET["usuario"]
    mensaje = "Bienvenido %r" %(EmailX)
    return HttpResponse(mensaje)

def registro(request):
    return render(request, 'store/register.html')

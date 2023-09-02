from django.shortcuts import render
from .carro import Carro
from tienda.models import Producto

# Al hacer cualquier cosa con el carro hay que direccionar la página de la tienda
from django.shortcuts import redirect

# Create your views here.


def agregar_producto(request, producto_id):
    # Crear carro
    carro = Carro(request)
    # Obtener el producto
    producto = Producto.objects.get(id=producto_id)
    # Agregar el producto al carro
    carro.agregar(producto=producto)

    return redirect("Tienda")


def eliminar_producto(request, producto_id):
    # Eliminar carro
    carro = Carro(request)
    # Obtener el producto
    producto = Producto.objects.get(id=producto_id)
    # Agregar el producto al carro
    carro.eliminar(producto=producto)

    return redirect("Tienda")


def restar_producto(request, producto_id):
    # Crear carro
    carro = Carro(request)
    # Obtener el producto
    producto = Producto.objects.get(id=producto_id)
    # Agregar el producto al carro
    carro.restar_producto(producto=producto)

    return redirect("Tienda")


def limpiar_carro(request, producto_id):
    # Crear carro
    carro = Carro(request)

    carro.limpiar_carro()

    return redirect("Tienda")

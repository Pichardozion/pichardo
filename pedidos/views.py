from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from flask import redirect

from pedidos.models import LineaPedido, Pedido
from carro.carro import Carro
from django.contrib import messages
from django.template.loader import render_to_string

from django.utils.html import strip_tags

from django.core.mail import send_mail

from .models import Producto


# Create your views here.


# Si no está logeado mandarlo a...
@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    # recorrer los elementos del carro uno a uno...
    carro = Carro(request)
    lineas_pedido = list()
    for key, value in carro.carro.items():
        lineas_pedido.append(
            LineaPedido(
                producto_id=key,
                cantidad=value["cantidad"],
                user=request.user,
                pedido=pedido,
            )
        )

    # Almacenar pedido:
    # Este método hacemuchos insert in to
    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.email,
    )

    messages.success(
        request,
        "Pedido realizado con éxito",
    )

    return redirect("../tienda")


def enviar_mail(**kwargs):
    asunto = "Gracias por su pedido"
    mensaje = render_to_string(
        "emails/pedido.html",
        {
            "pedido": kwargs.get("pedido"),
            "lineas_pedido": kwargs.get("lineas_pedido"),
            "nombreusuario": kwargs.get("nombreusuario"),
        },
    )
    mensaje_texto = strip_tags(mensaje)
    from_email = "22080081@upemor.edu.mx"
    # to = kwargs.get["emailusuario"]
    to = "pichardo.iandi@gmail.com"

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)

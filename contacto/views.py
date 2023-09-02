from django.shortcuts import render, redirect
from .forms import FormularioContacto

# Para configurar email
from django.core.mail import EmailMessage

# Create your views here.


def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage(
                "Mensaje desde  APP Django",
                "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(
                    nombre, email, contenido
                ),
                "",
                ["pichardo.iandi@gmail.com", "pablop@odtec.mx"],
                reply_to=[email],
            )

            try:
                email.send()

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?invalido")

    return render(
        request, "contacto/contacto.html", {"miFormulario": formulario_contacto}
    )

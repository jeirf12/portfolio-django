from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import send_mass_mail
from django.conf import settings
from django.contrib import messages

def home(request):
    name = 'jeirf12'
    return render(request, "home/home.html", { "title": "Soy el maestro %s" % name })

def contact(request):
    if request.method == "POST":
        name = request.POST["name_complete"]
        email = request.POST["email"]
        message = request.POST["message"]

        template_email = render_to_string("email/email_user.html", {
            'name': name,
            'email': email,
            'message': message,
        })

        template_email_user = render_to_string("email/email.html", {
            'name': name,
            'email': email,
            'message': message,
        })

        message_me = (
            "Solicitud Web Personal",
            template_email,
            email,
            [settings.EMAIL_HOST_USER],
        )

        message_his = (
            "Solicitud recibida",
            template_email_user,
            settings.EMAIL_HOST_USER,
            [email],
        )

        send_mass_mail((message_me, message_his), fail_silently = False)

        messages.success(request, 'El correo se ha enviado correctamente')
        return redirect('/')

    return render(request, "contact_me/contact_me.html")

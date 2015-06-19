 #!/usr/bin/python
 # -*- coding: latin-1 -*-


from django.http import *
import datetime
from django.shortcuts import render, render_to_response,redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login
from apps.barrio.models import Barrio, Hora


def index(request):
	html= "<html><body>Basura Zero</body></html>"
	return HttpResponse(html)

def index_admin(request):
	return render(request,'hola.html')




def login(request):
    if request.GET:
        username = request.GET['login']
        password = request.GET['password']
        user = authenticate(username=username, password=password)

        if user is not None:
           
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/main/')
            else:

                return HttpResponse("Your Rango account is disabled.")
        else:
            return HttpResponse("Usuario y/o Contraseña Incorrecta.")

    else:
    	return render_to_response('hola.html', context_instance= RequestContext(request))

def main(request):
	return render(request,'main.html')

def redirectBarrio(request):
    return render(request,'barrios.html')

def cargarBarrio(request):
    barr = Barrio(nombreBarrio = request.GET['barrio'])
    barr.save()
    return HttpResponse('Barrio creado con éxito!!')

def cargarHora(request):
    unaHora= Hora(date=request.GET['user_time'])
    unaHora.save()
    return HttpResponse('Hora cargada con éxito')







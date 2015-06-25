 #!/usr/bin/python
 # -*- coding: latin-1 -*-
from django.http import *
import datetime
from django.shortcuts import render, render_to_response,redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login
from apps.barrio.models import Barrio, Hora, Dia, Calle
import mysql.connector



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

def redirectHora(request):
    return render(request,'horarios.html')

def cargarHora(request):
    unahora=Hora(date= request.GET['user_time'])
    unahora.save()
    return HttpResponse('Hora cargada con éxito')

def redirectDia(request):
    return render(request, 'dia.html')

def cargarDia(request):
    unDia= Dia(dia= request.GET['dia'])
    unDia.save()
    return HttpResponse('Dia Cargado Exitosamente ')

def redirectCalle(request):
    x = Barrio.objects.all()
    context = {}
    context['b']=x
    a= Hora.objects.all()
    context['h']=a

    return render(request, 'calles.html',context)

def cargarDia(request):
    unDia= Dia(dia= request.GET['dia'])
    unDia.save()
    return HttpResponse('Calle Cargado Exitosamente ')

def cargarCalle(request):
    barrio = Barrio.objects.get(id = request.GET['barrio'])
    hora = Hora.objects.get(id = request.GET['hora'])
    unaCalle= Calle(nombreCalle= request.GET['calle'], nombreBarrio=barrio ,num_maximo= request.GET['max'], num_minimo= request.GET['min'], hora= hora)
    unaCalle.save()
    return HttpResponse('Calle Cargada Exitosamente ')








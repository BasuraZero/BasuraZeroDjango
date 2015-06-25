"""basurazero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.conf import settings
from apps.barrio.views import *

admin.autodiscover()

urlpatterns = [
	url(r'^admin/',include(admin.site.urls)),
	url(r'^',include(admin.site.urls)),
    url(r'^hola/',index),
    url(r'^index_admin/',login),
    url(r'^main/',main),
    url(r'^hola2/',redirectBarrio),
    url(r'^holaBarrio/',cargarBarrio),
    url(r'^hola3/',redirectHora),
    url(r'^hora/',cargarHora),
    url(r'^diaRedirect/',redirectDia),
    url(r'^dia/',cargarDia),
    url(r'^calleRedirect/',redirectCalle),
    url(r'^cargarCalle/',cargarCalle),






]

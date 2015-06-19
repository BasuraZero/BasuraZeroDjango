from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Barrio(models.Model):
	nombreBarrio= models.CharField(max_length=50)


	def __unicode__(self):
		return self.nombreBarrio


class Hora(models.Model):
	date = models.TimeField()

	def __unicode__(self):
		return unicode(self.date)

class Dia(models.Model):
	dia= models.CharField(max_length=20)

	def __unicode__(self):
		return self.dia


class Calle(models.Model):
	nombreCalle = models.CharField(max_length=50)
	nombreBarrio = models.ForeignKey(Barrio)
	num_maximo = models.IntegerField(blank=True, null=True)
	num_minimo= models.IntegerField(blank=True, null=True)
	hora= models.ForeignKey(Hora)
	dia= models.ManyToManyField(Dia)


	def __unicode__ (self):
		return self.nombreCalle









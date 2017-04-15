from __future__ import unicode_literals
from django.db import models


class Estado(models.Model):
	nombre = models.CharField(max_length=45)
	
	class Meta:
		ordering  = ('nombre',)
		app_label = 'mexico_bd'
	def __unicode__(self):
		return self.nombre

class Municipio(models.Model):
	clave  = models.CharField(max_length=6, primary_key = True)
	estado = models.ForeignKey(Estado)
	nombre = models.CharField(max_length=100)

	class Meta:
		ordering        = ('nombre',)
		app_label       = 'mexico_bd'
		unique_together = ('clave', 'estado',)
	def __unicode__(self):
		return self.nombre

class TipoAsentadera(models.Model):
	nombre = models.CharField(max_length=110)
	clave = models.IntegerField()

	class Meta:
		ordering  = ('nombre',)
		app_label = 'mexico_bd'
	def __unicode__(self):
		return self.nombre

class Zona(models.Model):
	nombre = models.CharField(max_length=110)

	class Meta:
		ordering  = ('nombre',)
		app_label = 'mexico_bd'
	def __unicode__(self):
		return self.nombre

class Asentadera(models.Model):
	clave          = models.CharField(max_length=7)
	tipo           = models.ForeignKey(TipoAsentadera)
	nombre         = models.CharField(max_length=110)
	cp  		   = models.CharField(max_length=7)	
	zona           = models.ForeignKey(Zona)
	municipio      = models.ForeignKey(Municipio,related_name='municipio')

	class Meta:
		ordering  = ('nombre',)
		app_label = 'mexico_bd'
	def __unicode__(self):
		return self.nombre
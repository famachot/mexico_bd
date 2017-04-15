# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework import status

from .models import Estado, Municipio, TipoAsentadera, Asentadera

class EstadoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Estado
		fields = ('id','nombre',)

class MunicipioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Municipio
		fields = ('clave','estado','nombre',)

class AsentaderaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Asentadera
		fields = ('clave','tipo','nombre', 'cp',)

class TipoAsentaderaSerializer(serializers.ModelSerializer):
	class Meta:
		model = TipoAsentadera
		fields = ('id', 'nombre', 'clave',)

		
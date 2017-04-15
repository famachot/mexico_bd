# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..utils.permissions import IsStaff

from .serializers import EstadoSerializer, TipoAsentaderaSerializer 
from .models import Estado, Municipio, TipoAsentadera, Asentadera, Zona


class EstadoView(viewsets.ModelViewSet):
	queryset = Estado.objects.all()
	serializer_class = EstadoSerializer
	model = Estado
	permission_classes = (IsStaff,)

class MunicipiosView(APIView):
	permission_classes = (IsStaff,)
	def get(self, request, pk, nom, format=None):
		municipios = [{'nombre': municipio.nombre, 
						'clave':municipio.clave} 
						for municipio in Municipio.objects.filter(
							estado=pk, nombre__icontains=nom)]
		return Response(municipios)


class AsentaderaView(APIView):
	permission_classes = (IsStaff,)
	def get(self, request, estado_id, municipio_id, nom, format = None):
		asentadera = [{'nombre': asentadera.nombre, 
						'clave':asentadera.clave, 
						'tipo': asentadera.tipo.nombre, 
						'cp': asentadera.cp} 
						for asentadera in Asentadera.objects.filter(
							municipio = municipio_id, 
							nombre__icontains=nom)]
		return Response(asentadera)


class CodigoPostal(APIView):
	permission_classes = (IsStaff,)
	def get(self, request, cp, format = None):
		data = {"municipio": {}, "estado": {}}
		print data
		data["asentadera"] = [{
						'id': asentadera.id,
						'nombre': asentadera.nombre, 
						'clave':asentadera.clave, 
						'cp': asentadera.cp} 
						for asentadera in Asentadera.objects.filter(
							cp = cp)]
		if(len(data["asentadera"]) > 0):
			asentadera = Asentadera.objects.get(pk = data["asentadera"][0]["id"])
			print asentadera.municipio
			data["municipio"]["nombre"] = asentadera.municipio.nombre
			data["municipio"]["clave"] = asentadera.municipio.clave
			data["estado"]["nombre"] = asentadera.municipio.estado.nombre
			data["estado"]["id"] = asentadera.municipio.estado.id
		return Response(data)


class TipoAsentadera(APIView):
	permission_classes = (IsStaff,)
	def get(self, request, pk, format = None):
		try:
			asentadera = Asentadera.objects.get(pk = pk)
		except Asentadera.DoesNotExist:
			content = {'ID': 'El elemento solicitado no existe'}
			return Response(content, status=status.HTTP_404_NOT_FOUND)
		serializer = TipoAsentaderaSerializer(asentadera.tipo, many=False)
 		return Response(serializer.data)

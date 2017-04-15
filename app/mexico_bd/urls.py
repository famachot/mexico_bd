# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'estado', views.EstadoView, 'list')

urlpatterns = [
    url(r'ubicacion/', include(router.urls)),
    url(r'ubicacion/estado/(?P<pk>[0-9]+)/municipio/(?P<nom>[A-Za-z]+)/$',views.MunicipiosView.as_view()),
    url(r'ubicacion/estado/(?P<estado_id>[0-9]+)/municipio/(?P<municipio_id>[0-9]+)/(?P<nom>[A-Za-z]+)/$',views.AsentaderaView.as_view()),
   	url(r'ubicacion/cp/(?P<cp>[0-9]+)/$', views.CodigoPostal.as_view()),
   	url(r'ubicacion/asentadera/(?P<pk>[0-9]+)/tipo/$', views.TipoAsentadera.as_view())
]
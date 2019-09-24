from django.shortcuts import render
from rest_framework import viewsets
from landing.models import Heroi, Universo, Arq_vilao, Habilidade
from landing.serializer import HabilidadeSerializer, Arq_vilaoSerializer


class HeroiViewSet(viewsets.ModelViewSet):
    queryset = Heroi.objects.all()
    serializer_class = Heroi


class UniversoViewSet(viewsets.ModelViewSet):
    queryset = Universo.objects.all()
    serializer_class = Universo


class HabilidadeViewSet(viewsets.ModelViewSet):
    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer


class Arq_vilaoViewSet(viewsets.ModelViewSet):
    queryset = Arq_vilao.objects.all()
    serializer_class = Arq_vilaoSerializer

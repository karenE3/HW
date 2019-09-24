from django.db.migrations import serializer
from rest_framework import serializers
from landing.models import Heroi, Universo, Habilidade, Arq_vilao


class UniversoSerializer(serializer.Models.Serializer):
    class Meta:
        model = Universo
        fields = '__all__'


class HeroiSerializer(serializers.Models.Serializer):
    class Meta:
        model = Heroi
        fields = '__all__'


class HabilidadeSerializer(serializers.Models.Serializer):
    class Meta:
        model = Habilidade
        fields = '__all__'


class Arq_vilaoSerializer(serializers.Models.Serializer):
    class Meta:
        model = Arq_vilao
        fields = '__all__'

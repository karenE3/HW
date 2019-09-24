from django.db import models


class Universo(models.Model):
    nome = models.CharField(max_length=255)


class Heroi(models.Model):
    nome = models.CharField(
        max_length=255
    )
    fraqueza = models.CharField(
        max_length=255
    )
    universo = models.CharField(
        max_length=255
    )


class Habilidade(models.Model):
    nome = models.CharField(
        max_length=255
    )
    nivel_hab = models.CharField(
        max_length=255
    )

    nivel_habilidade = models.IntegerField()
    hab_heroi = models.ManyToManyField(Heroi, related_name='habilidade')


class Arq_vilao(models.Model):
    nome = models.CharField(
        max_length=255
    )

    universo = models.ForeignKey(Universo, on_delete=models.CASCADE)
    heroi = models.ForeignKey(Heroi, on_delete=models.CASCADE)
    hab_vilao = models.ManyToManyField(Habilidade, related_name='arg_vilao')

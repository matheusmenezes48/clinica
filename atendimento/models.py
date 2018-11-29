from django.db import models

class Cliente(models.Model):
    NOME = models.CharField(max_length=50)
    DT_NASC = models.DateField()
    CPF = models.CharField(max_length=11)
    SEXO = models.CharField(max_length=1)

class Medico(models.Model):
    NOME = models.CharField(max_length=50)
    DT_NASC = models.DateField()
    ESPECIALIDADE = models.CharField(max_length=25)
    SEXO = models.CharField(max_length=1)


from django.db import models
from usuarios.models import Usuario


class Area(models.Model):
    area = models.CharField(max_length=100, null=False)


class SubArea(models.Model):
    subarea = models.CharField(max_length=100, null=False)
    area = models.ForeignKey(Area)


class Termo(models.Model):
    termo = models.CharField(max_length=100, null=False)
    subarea = models.ForeignKey(SubArea)
    img = models.ImageField(upload_to="/imagens")
    expressao = models.CharField(max_length=200, null=False)
    aprovado = models.BooleanField(default=True)


class Sugestao(models.Model):
    termo = models.ForeignKey(Termo)
    usuario = models.ForeignKey(Usuario) #o usuário que sugeriu o termo
    timestamp = models.DateTimeField(auto_now_add=True)

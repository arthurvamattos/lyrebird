from django.db import models
from usuarios.models import Usuario


class Area(models.Model):
    area = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.area}'


class SubArea(models.Model):
    subarea = models.CharField(max_length=100, null=False)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.area}:{self.subarea}'


class Termo(models.Model):
    termo = models.CharField(max_length=100, null=False)
    subarea = models.ForeignKey(SubArea, on_delete=models.SET_NULL, null=True)
    img = models.ImageField(upload_to="imagens/")
    expressao = models.CharField(max_length=200, null=False)
    aprovado = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.subarea}:{self.termo}'


class Sugestao(models.Model):
    termo = models.ForeignKey(Termo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) #o usuário que sugeriu o termo
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.termo.subarea}:{self.termo}'

from django.db import models


class Config(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.CharField(max_length=255)

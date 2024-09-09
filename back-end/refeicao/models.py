from django.db import models


class Refeicao(models.Model):
    nome = models.CharField(max_length=100, null=True)
    ativo = models.BooleanField(default=True)

class ConfigRefeicao(models.Model):
    refeicao = models.ForeignKey(Refeicao, on_delete=models.CASCADE)
    dias_semana = models.ForeignKey('DiasSemana', on_delete=models.CASCADE)
    categoria_receita = models.ForeignKey('receita.CategoriaReceita', on_delete=models.CASCADE)

class DiasSemana(models.Model):
    nome = models.CharField(max_length=100)
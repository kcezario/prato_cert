from django.db import models


class Receita(models.Model):
    nome = models.CharField(max_length=100)
    inativo = models.BooleanField(default=False)


class Ingrediente(models.Model):
    loja = models.ForeignKey('loja.Loja', on_delete=models.CASCADE)
    categoria_ingrediente = models.ForeignKey('CategoriaIngrediente', on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=100)
    inativo = models.BooleanField(default=False)


class CategoriaReceita(models.Model):
    nome = models.CharField(max_length=100)
    inativo = models.BooleanField(default=False)


class CategoriaIngrediente(models.Model):
    nome = models.CharField(max_length=100)
    inativo = models.BooleanField(default=False)


class ReceitaIngrediente(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)


class ReceitaCategoriaReceita(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    categoria_receita = models.ForeignKey(CategoriaReceita, on_delete=models.CASCADE)

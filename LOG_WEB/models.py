from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.

class Motorista(models.Model):
    STATUS_CHOICES = [
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    ]
    nome = models.CharField(max_length=80)
    cpf = models.CharField(max_length=20, null=False, unique=True)
    telefone = models.CharField(max_length=20)
    cidade = models.CharField(max_length=40)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='Ativo')
    observacao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Estabelecimento(models.Model):
    STATUS_CHOICES = [
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='Ativo')
    nome = models.CharField(max_length=80)
    cnpj = models.CharField(max_length=20, null=False, unique=True)
    cidade = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Colaborador(models.Model):
    STATUS_CHOICES = [
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='Ativo')
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=80)
    email = models.EmailField(max_length=254, blank=True)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    observacao = models.TextField(blank=True)



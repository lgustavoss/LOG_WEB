from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.

class Motorista(models.Model):
    STATUS_CHOICES = [
        ('Ativo', 'ativo'),
        ('Inativo', 'inativo'),
    ]
    nome = models.CharField(max_length=80)
    cpf = models.CharField(max_length=20, null=False, unique=True)
    telefone = models.CharField(max_length=20)
    cidade = models.CharField(max_length=40)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='Ativo')
    observacao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


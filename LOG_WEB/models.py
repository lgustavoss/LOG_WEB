from django.db import models


# Create your models here.

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

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name_plural = "Colaboradores"


class Adquirente(models.Model):
    adquirente = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.adquirente


class Modelomaquininha(models.Model):
    modelo = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.modelo

    class Meta:
        verbose_name = "Modelo Maquininha"
        verbose_name_plural = "Modelos Maquininhas"


class Maquininha(models.Model):
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelomaquininha, on_delete=models.CASCADE)
    adquirente = models.ForeignKey(Adquirente, on_delete=models.CASCADE)
    n_logico = models.CharField(max_length=40, unique=True)
    terminal = models.CharField(max_length=40, unique=True)
    data_ativacao = models.DateField()
    os_ativacao = models.CharField(max_length=30)
    data_inativacao = models.DateField(blank=True, null=True, default=None)
    os_inativacao = models.CharField(blank=True, max_length=30, null=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.n_logico


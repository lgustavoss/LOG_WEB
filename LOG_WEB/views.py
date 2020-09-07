from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import *


# Create your views here.
# Criar, listar e editar Estabelecimentos
class EstabelecimentoForm(ModelForm):
    class Meta:
        model = Estabelecimento
        fields = ['status', 'nome', 'cnpj', 'cidade']


def listar_estabelecimento(request, template_name='listar_estabelecimento.html'):
    query = request.GET.get("busca")
    if query:
        estabelecimento = Estabelecimento.objects.filter(nome_incontains=query)
    else:
        estabelecimento = Estabelecimento.objects.all()
    estabelecimentos = {'lista': estabelecimento}
    return render(request, template_name, estabelecimentos)


def cadastrar_estabelecimento(request, template_name='cadastrar_estabelecimento.html'):
    form = EstabelecimentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_estabelecimento')
    return render(request, template_name, {'form': form})


def editar_estabelecimento(request, pk, template_name='cadastrar_estabelecimento.html'):
    estabelecimento = get_object_or_404(Estabelecimento, pk=pk)
    if request.method == "POST":
        form = EstabelecimentoForm(request.POST, instance=estabelecimento)
        if form.is_valid():
            form.save()
            return redirect('listar_estabelecimento')
    else:
        estabelecimento = EstabelecimentoForm(instance=estabelecimento)
    return render(request, template_name, {'form': estabelecimento})


# Criar, listar e editar Colaboradores

class ColaboradorForm(ModelForm):
    class Meta:
        model = Colaborador
        fields = ['status', 'nome', 'funcao', 'email', 'estabelecimento', 'observacao']


def listar_colaborador(request, template_name='listar_colaborador.html'):
    query = request.GET.get("busca")
    if query:
        colaborador = Colaborador.objects.filter(nome_incontains=query)
    else:
        colaborador = Colaborador.objects.all()
    colaboradores = {'lista': colaborador}
    return render(request, template_name, colaboradores)


def cadastrar_colaborador(request, template_name='cadastrar_colaborador.html'):
    form = ColaboradorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_colaborador')
    return render(request, template_name, {'form': form})


def editar_colaborador(request, pk, template_name='cadastrar_colaborador.html'):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == "POST":
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            return redirect('listar_colaborador')
    else:
        form = ColaboradorForm(instance=colaborador)
    return render(request, template_name, {'form': form})


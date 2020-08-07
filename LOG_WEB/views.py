from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import *


# Create your views here.

class EstabelecimentoForm(ModelForm):
    class Meta:
        model = Estabelecimento
        fields = ['status', 'nome', 'cnpj', 'cidade']


def listar_estabelecimento(request, template_name='estabelecimento_list.html'):
    query = request.GET.get("busca")
    if query:
        estabelecimento = Estabelecimento.objects.filter(nome_incontains=query)
    else:
        estabelecimento = Estabelecimento.objects.all()
    estabelecimentos = {'lista': estabelecimento}
    return render(request, template_name, estabelecimentos)


def cadastrar_estabelecimento(request, template_name='estabelecimento_form.html'):
    form = EstabelecimentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('estabelecimento_list')
    return render(request, template_name, {'form': form})


def editar_estabelecimento(request, pk, template_name='estabelecimento_form.html'):
    estabelecimento = get_object_or_404(Estabelecimento, pk=pk)
    if request.method == "POST":
        form = EstabelecimentoForm(request.POST, instance=estabelecimento)
        if form.is_valid():
            form.save()
            return redirect('estabelecimento_list')
    else:
        form = EstabelecimentoForm(instance=estabelecimento)
    return render(request, template_name, {'form': form})



"""
Configuração das views do projeto
"""
from django.shortcuts import render


def index(request):
    """
    View responsável pela renderização do template index
    """
    return render(request, "index.html")


def contato(request):
    """
    View responsável pela renderização do template contato
    """
    return render(request, "contato.html")


def produto(request):
    """
    View responsável pela renderização do template produto
    """
    return render(request, "produto.html")

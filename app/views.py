from django.db.models import Prefetch
from django.shortcuts import render

from .models import Cliente, Pedido, ItemPedido, Categoria


def lista_clientes(request):
    clientes = Cliente.objects.select_related('endereco').prefetch_related(
        Prefetch(
            'pedidos',
            queryset=Pedido.objects.prefetch_related(
                Prefetch('itens', queryset=ItemPedido.objects.select_related('produto'))
            )
        )
    )
    return render(request, 'lista_clientes.html', {'clientes': clientes})


def lista_categorias(request):
    categorias = Categoria.objects.prefetch_related('produtos')
    return render(request, 'lista_categorias.html', {'categorias': categorias})

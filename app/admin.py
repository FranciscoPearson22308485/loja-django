from django.contrib import admin

from .models import Categoria, Produto, Endereco, Cliente, Pedido, ItemPedido


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1


class PedidoAdmin(admin.ModelAdmin):
    inlines = [ItemPedidoInline]


admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Endereco)
admin.site.register(Cliente)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido)

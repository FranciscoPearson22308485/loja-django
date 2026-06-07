from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name='produtos'
    )

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    rua = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.rua}, {self.cidade}'


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.OneToOneField(
        Endereco, on_delete=models.CASCADE, related_name='cliente'
    )

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name='pedidos'
    )
    data = models.DateField(auto_now_add=True)
    produtos = models.ManyToManyField(
        Produto, through='ItemPedido', related_name='pedidos'
    )

    def __str__(self):
        return f'Pedido #{self.id} - {self.cliente.nome}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido, on_delete=models.CASCADE, related_name='itens'
    )
    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE, related_name='itens'
    )
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.produto.nome} x{self.quantidade}'

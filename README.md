# Loja Django — Exercício 13

## Modelos

- Categoria 1:N Produto
- Cliente 1:1 Endereco
- Cliente 1:N Pedido
- Pedido N:M Produto via ItemPedido (com quantidade)

## Vistas

- `/clientes/` — clientes com pedidos e itens (produto + quantidade + preço)
- `/categorias/` — categorias com os seus produtos

## Dados de teste (ordem obrigatória no admin)

1. Categorias → 2. Endereços → 3. Clientes → 4. Produtos → 5. Pedidos (com ItemPedido inline)

## Setup

```bash
python manage.py migrate && python manage.py createsuperuser && python manage.py runserver
```

**Autor:** Francisco Pearson — 22308485 | Universidade Lusófona · PW 2025/26

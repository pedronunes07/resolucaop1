from django.contrib import admin
from .models import Todo, Produto, Categoria, Fornecedor, MovimentacaoEstoque

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'telefone', 'email')
    search_fields = ('nome', 'cnpj', 'email')
    list_filter = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero_serie', 'categoria', 'quantidade', 'preco_custo', 'preco_venda', 'ativo')
    list_filter = ('categoria', 'fornecedor', 'ativo')
    search_fields = ('nome', 'numero_serie')
    readonly_fields = ('data_entrada',)

@admin.register(MovimentacaoEstoque)
class MovimentacaoEstoqueAdmin(admin.ModelAdmin):
    list_display = ('produto', 'tipo', 'quantidade', 'data', 'usuario')
    list_filter = ('tipo', 'data', 'usuario')
    search_fields = ('produto__nome', 'observacao')
    readonly_fields = ('data',)

admin.site.register(Todo)

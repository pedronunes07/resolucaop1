from django.urls import path
from .views import (
    ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView,
    CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView,
    FornecedorListView, FornecedorCreateView, FornecedorUpdateView, FornecedorDeleteView,
    MovimentacaoEstoqueListView, movimentacao_estoque_create,
    login_view, logout_view, cadastro_view, sobre_view
)

urlpatterns = [
    path('produtos/', ProdutoListView.as_view(), name='produto_list'),
    path('produtos/novo/', ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/<int:pk>/remover/', ProdutoDeleteView.as_view(), name='produto_delete'),
    
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/nova/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/remover/', CategoriaDeleteView.as_view(), name='categoria_delete'),
    
    path('fornecedores/', FornecedorListView.as_view(), name='fornecedor_list'),
    path('fornecedores/novo/', FornecedorCreateView.as_view(), name='fornecedor_create'),
    path('fornecedores/<int:pk>/editar/', FornecedorUpdateView.as_view(), name='fornecedor_update'),
    path('fornecedores/<int:pk>/remover/', FornecedorDeleteView.as_view(), name='fornecedor_delete'),
    
    path('movimentacoes/', MovimentacaoEstoqueListView.as_view(), name='movimentacao_list'),
    path('movimentacoes/nova/', movimentacao_estoque_create, name='movimentacao_create'),
    
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('sobre/', sobre_view, name='sobre')
] 
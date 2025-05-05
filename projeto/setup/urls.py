from django.contrib import admin
from django.urls import path
from todos import views
from todos.views import (
    TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView,
    ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  # Página inicial é o login
    path('lista/', TodoListView.as_view(), name='todo_list'),  # Lista de tarefas
    path('create/', TodoCreateView.as_view(), name='todo_create'),  # Criação de tarefa
    path('update/<int:pk>/', TodoUpdateView.as_view(), name="todo_update"),  # Edição de tarefa
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name="todo_delete"),  # Deleção de tarefa
    path('servico/', views.todo_servico_view, name='todo_servico'),  # Página de serviços
    path('logout/', views.logout_view, name='logout'),  # Logout
    path('cadastro/', views.cadastro_view, name='cadastro'),  # Cadastro de usuário
    path('sobre/', views.sobre_view, name='sobre'),  # Página "Sobre" (novamente, você deve adicionar a view)
    
    # URLs para Produtos
    path('produtos/', ProdutoListView.as_view(), name='produto_list'),
    path('produtos/novo/', ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/<int:pk>/remover/', ProdutoDeleteView.as_view(), name='produto_delete'),
]

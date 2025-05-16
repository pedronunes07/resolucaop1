from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from todos import views
from todos.views import (
    TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView,
    ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView,
    dashboard
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  # Página inicial é o login
    path('dashboard/', dashboard, name='dashboard'),  # Dashboard
    path('lista/', TodoListView.as_view(), name='todo_list'),  # Lista de tarefas
    path('create/', TodoCreateView.as_view(), name='todo_create'),  # Criação de tarefa
    path('update/<int:pk>/', TodoUpdateView.as_view(), name="todo_update"),  # Edição de tarefa
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name="todo_delete"),  # Deleção de tarefa
    path('servico/', views.todo_servico_view, name='todo_servico'),  # Página de serviços
    path('logout/', views.logout_view, name='logout'),  # Logout
    path('cadastro/', views.cadastro_view, name='cadastro'),  # Cadastro de usuário
    path('sobre/', views.sobre_view, name='sobre'),  # Página "Sobre"
    
    # Inclui todas as URLs do app todos
    path('', include('todos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

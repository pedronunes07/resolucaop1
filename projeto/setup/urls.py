from django.contrib import admin
from django.urls import path
from todos import views
from todos.views import (
    TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  # Página inicial agora é o login
    path('lista/', TodoListView.as_view(), name='todo_list'),
    path('create/', TodoCreateView.as_view(), name='todo_create'),
    path('update/<int:pk>/', TodoUpdateView.as_view(), name="todo_update"),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name="todo_delete"),
    path('servico/', views.todo_servico_view, name='todo_servico'),  # Página de serviços
    path('login/', views.login_view, name='login'),  # Página de login
    path('logout/', views.logout_view, name='logout'),  # Logout
    path('cadastro/', views.cadastro_view, name='cadastro'),  # Cadastro
]
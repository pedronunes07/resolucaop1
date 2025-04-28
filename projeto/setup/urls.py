# todos/urls.py

from django.contrib import admin
from django.urls import path
from todos.views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView, TodoServicoView, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TodoListView.as_view(), name='todo_list'),
    path('create/', TodoCreateView.as_view(), name='todo_create'),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path('servico/', TodoServicoView.as_view(), name='todo_servico'),  # Página de serviços
    path('login/', login_view, name='login') # Página de login
]

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from .models import Todo
from django.urls import reverse_lazy

# Suas views existentes
class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

# View para a página de serviço
class TodoServicoView(TemplateView):
    template_name = 'todos/todo_servico.html'

# View para a página de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Tenta autenticar o usuário
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Realiza o login do usuário
            return redirect('todo_servico')  # Redireciona para a página de serviços após o login
        else:
            # Caso falhe a autenticação
            return render(request, 'todo_list.html', {'error': 'Usuário ou senha inválidos'})

    return render(request, 'todo_list.html')

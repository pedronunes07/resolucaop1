from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Todo

# Views existentes
class TodoListView(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")
    template_name = 'todos/todo_form.html'

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")
    template_name = 'todos/todo_form.html'

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")
    template_name = 'todos/todo_confirm_delete.html'

# View para a página de serviço (protegida por login)
@login_required(login_url='/login/')
def todo_servico_view(request):
    return render(request, 'todos/todo_servico.html')

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
            messages.error(request, 'Usuário ou senha inválidos')
            return render(request, 'todos/login.html', {'error': 'Usuário ou senha inválidos'})

    return render(request, 'todos/login.html')

# View para logout
def logout_view(request):
    logout(request)
    return redirect('login')

# View para cadastro de usuário
def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        username = request.POST.get('nome-usuario')
        email = request.POST.get('email')
        password = request.POST.get('senha')
        confirm_password = request.POST.get('confirmar-senha')
        
        # Validações básicas
        if password != confirm_password:
            messages.error(request, 'As senhas não coincidem')
            return render(request, 'todos/cadastro.html', {'error': 'As senhas não coincidem'})
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe')
            return render(request, 'todos/cadastro.html', {'error': 'Nome de usuário já existe'})
            
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado')
            return render(request, 'todos/cadastro.html', {'error': 'Email já cadastrado'})
        
        # Criar o usuário
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=nome
            )
            messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Erro ao criar usuário: {str(e)}')
            return render(request, 'todos/cadastro.html', {'error': f'Erro ao criar usuário: {str(e)}'})
    
    return render(request, 'todos/cadastro.html')

def sobre_view(request):
    return render(request, 'todos/sobre.html')
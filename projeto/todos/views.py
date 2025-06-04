from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Sum, F
from django.utils import timezone
from .models import Produto, Categoria, Fornecedor, MovimentacaoEstoque
from django.http import HttpResponse

# View para a página de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Tenta autenticar o usuário
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Realiza o login do usuário
            return redirect('produto_list')  # Redireciona para a página de produtos após o login

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

class ProdutoListView(ListView):
    model = Produto
    template_name = 'todos/produto_list.html'

class ProdutoCreateView(CreateView):
    model = Produto
    fields = ["nome", "numero_serie", "quantidade", "imagem"]
    success_url = reverse_lazy("produto_list")
    template_name = 'todos/produto_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Produto criado com sucesso!')
        return response

class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ["nome", "numero_serie", "quantidade", "imagem"]
    success_url = reverse_lazy("produto_list")
    template_name = 'todos/produto_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Produto atualizado com sucesso!')
        return response

class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy("produto_list")
    template_name = 'todos/produto_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(request, 'Produto excluído com sucesso!')
        return response

# Views para Categoria
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'todos/categoria_list.html'
    context_object_name = 'categorias'

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['nome', 'descricao']
    success_url = reverse_lazy('categoria_list')
    template_name = 'todos/categoria_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Categoria criada com sucesso!')
        return response

class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ['nome', 'descricao']
    success_url = reverse_lazy('categoria_list')
    template_name = 'todos/categoria_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Categoria atualizada com sucesso!')
        return response

class CategoriaDeleteView(DeleteView):
    model = Categoria
    success_url = reverse_lazy('categoria_list')
    template_name = 'todos/categoria_confirm_delete.html'

# Views para Fornecedor
class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'todos/fornecedor_list.html'
    context_object_name = 'fornecedores'

class FornecedorCreateView(CreateView):
    model = Fornecedor
    fields = ['nome', 'cnpj', 'telefone', 'email', 'endereco']
    success_url = reverse_lazy('fornecedor_list')
    template_name = 'todos/fornecedor_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Fornecedor cadastrado com sucesso!')
        return response

class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    fields = ['nome', 'cnpj', 'telefone', 'email', 'endereco']
    success_url = reverse_lazy('fornecedor_list')
    template_name = 'todos/fornecedor_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Fornecedor atualizado com sucesso!')
        return response

class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    success_url = reverse_lazy('fornecedor_list')
    template_name = 'todos/fornecedor_confirm_delete.html'

# Views para Movimentação de Estoque
class MovimentacaoEstoqueListView(ListView):
    model = MovimentacaoEstoque
    template_name = 'todos/movimentacao_list.html'
    context_object_name = 'movimentacoes'
    ordering = ['-data']

@login_required
def movimentacao_estoque_create(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto')
        tipo = request.POST.get('tipo')
        quantidade = int(request.POST.get('quantidade'))
        observacao = request.POST.get('observacao')
        
        produto = get_object_or_404(Produto, id=produto_id)
        
        if tipo == 'SAIDA' and quantidade > produto.quantidade:
            messages.error(request, 'Quantidade insuficiente em estoque!')
            return redirect('movimentacao_create')
        
        movimentacao = MovimentacaoEstoque.objects.create(
            produto=produto,
            tipo=tipo,
            quantidade=quantidade,
            observacao=observacao,
            usuario=request.user
        )
        
        # Atualiza a quantidade do produto
        if tipo == 'ENTRADA':
            produto.quantidade += quantidade
        else:
            produto.quantidade -= quantidade
        
        produto.save()
        messages.success(request, 'Movimentação registrada com sucesso!')
        return redirect('movimentacao_list')
    
    produtos = Produto.objects.filter(ativo=True)
    return render(request, 'todos/movimentacao_form.html', {'produtos': produtos})

# Dashboard
@login_required
def dashboard(request):
    total_produtos = Produto.objects.count()
    total_valor_estoque = Produto.objects.aggregate(
        total=Sum(F('quantidade') * F('preco_custo'))
    )['total'] or 0
    
    produtos_baixo_estoque = Produto.objects.filter(
        quantidade__lte=F('quantidade_minima')
    ).count()
    
    ultimas_movimentacoes = MovimentacaoEstoque.objects.select_related(
        'produto', 'usuario'
    ).order_by('-data')[:5]
    
    context = {
        'total_produtos': total_produtos,
        'total_valor_estoque': total_valor_estoque,
        'produtos_baixo_estoque': produtos_baixo_estoque,
        'ultimas_movimentacoes': ultimas_movimentacoes,
    }
    
    return render(request, 'todos/dashboard.html', context)

# View de teste temporária
def teste_view(request):
    return HttpResponse("Hello, Render!")
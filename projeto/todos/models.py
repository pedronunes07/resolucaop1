from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.utils import timezone

class Categoria(models.Model):
	nome = models.CharField(max_length=100, null=False, blank=False)
	descricao = models.TextField(null=True, blank=True)
	
	def __str__(self):
		return self.nome
	
	class Meta:
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'

class Fornecedor(models.Model):
	nome = models.CharField(max_length=100, null=False, blank=False)
	cnpj = models.CharField(max_length=18, null=True, blank=True)
	telefone = models.CharField(max_length=20, null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	endereco = models.TextField(null=True, blank=True)
	
	def __str__(self):
		return self.nome
	
	class Meta:
		verbose_name = 'Fornecedor'
		verbose_name_plural = 'Fornecedores'

class Produto(models.Model):
	nome = models.CharField(max_length=100, null=False, blank=False)
	numero_serie = models.CharField(max_length=50, null=False, blank=False, unique=True)
	descricao = models.TextField(null=True, blank=True)
	categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True)
	fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, null=True)
	quantidade = models.IntegerField(null=False, blank=False, default=0)
	quantidade_minima = models.IntegerField(null=False, blank=False, default=5)
	preco_custo = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
	preco_venda = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
	localizacao = models.CharField(max_length=50, null=True, blank=True)
	imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
	data_entrada = models.DateField(default=timezone.now)
	data_validade = models.DateField(null=True, blank=True)
	ativo = models.BooleanField(default=True)
	
	def __str__(self):
		return self.nome
	
	def valor_total_estoque(self):
		return self.quantidade * self.preco_custo
	
	def precisa_reposicao(self):
		return self.quantidade <= self.quantidade_minima
	
	class Meta:
		verbose_name = 'Produto'
		verbose_name_plural = 'Produtos'

class MovimentacaoEstoque(models.Model):
	TIPO_CHOICES = [
		('ENTRADA', 'Entrada'),
		('SAIDA', 'Saída'),
	]
	
	produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
	tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
	quantidade = models.IntegerField(null=False, blank=False)
	data = models.DateTimeField(auto_now_add=True)
	observacao = models.TextField(null=True, blank=True)
	usuario = models.ForeignKey('auth.User', on_delete=models.PROTECT)
	
	def __str__(self):
		return f"{self.tipo} - {self.produto.nome} - {self.quantidade}"
	
	class Meta:
		verbose_name = 'Movimentação de Estoque'
		verbose_name_plural = 'Movimentações de Estoque'

# Create your models here.

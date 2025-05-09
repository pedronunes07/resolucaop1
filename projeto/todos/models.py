from django.db import models

class Todo(models.Model):
	title = models.CharField(max_length=100, null=False, blank=False)
	created_at =models.DateField(auto_now_add=True,null=False,blank=False)
	deadline = models.DateField(null=False, blank=False)
	finished_at = models.DateField(null=True)

class Produto(models.Model):
	nome = models.CharField(max_length=100, null=False, blank=False)
	numero_serie = models.CharField(max_length=50, null=False, blank=False)
	quantidade = models.IntegerField(null=False, blank=False)
	imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)

# Create your models here.

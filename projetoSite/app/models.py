from django.db import models

# Create your models here.

class Usuario(models.Model):
    SEXO_CHOICES = (
        ("feminino", "Feminino"),
        ("masculino", "Masculino"),
    )
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50,null=False)
    email = models.EmailField(max_length=30, null=False)
    data_nascimento = models.DateField(null=False,verbose_name="Data de Nascimento")
    cpf = models.CharField(max_length=20, null=False)
    sexo = models.CharField(max_length=20,null=False,choices=SEXO_CHOICES)
    telefone = models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50, null=False)
    quantidade = models.IntegerField(max_length=100)
    valor = models.FloatField(null=False)
    foto_capa = models.ImageField(upload_to='images')

    def __str__(self):
        return self.nome

class PedidoRegistro(models.Model):
    id = models.IntegerField(primary_key=True)
    dataPedido = models.DateField(null=False)
    valorTotal = models.FloatField(null=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    produto = models.ManyToManyField(Produto)

    def __str__(self):
        return self.id
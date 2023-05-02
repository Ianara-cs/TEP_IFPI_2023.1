from django.contrib.auth.models import User
from django.db import models


class Investor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )

    choices_perfil = (
        ('A', 'Arrojado'),
        ('C', 'Conservador'),
        ('M', 'Moderado'),
    )
    perfil = models.CharField(max_length=1, choices=choices_perfil)


#def validate_cod(value):
#    for i in list(value):
#        if i % 2 != 0:
        

class Stock(models.Model):
    cod = models.CharField(unique=True, max_length=60)
    nome_empresa = models.CharField(max_length=60)
    cnpj = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.cod
    


class Transaction(models.Model):
    data = models.DateField(auto_now_add=True)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantidade_acoes = models.IntegerField()
    choices_tipo = (
        ('C', 'Compra'),
        ('V', 'Venda'),
    )
    tipo = models.CharField(max_length=1, choices=choices_tipo)
    corretagem = models.FloatField()
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
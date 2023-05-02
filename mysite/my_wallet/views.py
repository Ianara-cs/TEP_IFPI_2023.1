from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .models import Investor, Stock, Transaction


def cadastro_transacao(request):
    stocks = Stock.objects.filter()
    context = {
        'ativos': stocks,
    }
    return render(request, 'cadastrar_transacao.html', context=context)

@login_required
def cadastrar_perfil(request):
    user = request.user
    print(user)
    return render(request, 'cadastrar_perfil.html')

@login_required
def validar_perfil(request):
    user = request.user
    print(user)
    tipo= request.POST['tipo_perfil']

    try:
        perfil = Investor(perfil=tipo, user=user)
        perfil.save()
        return redirect('cadastro_transacao')
    except:
        return redirect('cadastra_perfil')

def valida_transacao(request):
    tipo= request.POST['tipo_operacao']
    ativo = request.POST['ativo']
    quantidade = request.POST['quantidade']
    preco = request.POST['preco']
    corretagem = request.POST['corretagem']
    data = request.POST['data']

    stock = Stock.objects.filter(cod = ativo)
    print(stock[0])

    transacao = Transaction.objects.create(
        tipo=tipo, stock=stock[0], quantidade_acoes=quantidade, corretagem=corretagem, data=data
    )

    return HttpResponse(transacao)

def lista_ativos(request, cod):

    stocks = Stock.objects.filter(cod = cod)
    context = {
        'ativos': stocks,
    }
    
    return HttpResponseGone(stocks)
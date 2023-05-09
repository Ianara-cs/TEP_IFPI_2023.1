from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .models import Investor, Stock, Transaction


@login_required
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
    tipo = request.POST['tipo_perfil']

    try:
        perfil = Investor(perfil=tipo, user=user)
        perfil.save()
        return redirect('cadastro_transacao')
    except:
        return redirect('cadastra_perfil')

@login_required
def valida_transacao(request):
    user = request.user
    tipo= request.POST['tipo_operacao']
    ativo = request.POST['ativo']
    quantidade = request.POST['quantidade']
    preco = request.POST['preco']
    corretagem = request.POST['corretagem']
    data = request.POST['data']

    try:
        stock = Stock.objects.get(cod = ativo)
        investor = Investor.objects.get(user = user)
        print(stock)

        transacao = Transaction.objects.create(
            tipo=tipo, stock=stock, quantidade_acoes=quantidade, corretagem=corretagem, data=data, investor=investor
        )

        return HttpResponse(transacao)
    except:
        return redirect('cadastro_transacao')

def transacoes(request):
    user = request.user
    investor = Investor.objects.get(user = user)
    transactions = Transaction.objects.filter(investor = investor)
    context = {
        'transactions': transactions,
    }

    return render(request, 'transactions.html', context=context)

def detalhesTransacoes(request, id: int):
    transactions = Transaction.objects.get(id=id)

    context = {
        'transactions': transactions,
    }

    return render(request, 'detalhes.html', context=context)
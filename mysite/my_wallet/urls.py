from django.urls import path

from . import views

urlpatterns = [
    path('cadastro_transacao/', views.cadastro_transacao, name = 'cadastro_transacao'),
    path('valida_transacao/', views.valida_transacao, name = 'valida_transacao'),
    path('cadastra_perfil/', views.cadastrar_perfil, name = 'cadastra_perfil'),
    path('valida_perfil/', views.validar_perfil, name = 'valida_perfil'),
    path('transacoes/', views.transacoes, name = 'transacoes'),
    path('transacoes/<int:id>/', views.detalhesTransacoes, name = 'detalhes')
]
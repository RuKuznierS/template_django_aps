from django.urls import path
from app_notas import views

urlpatterns = [
    path('', views.home, name="home"),
    path('produtos/', views.produtos, name="produtos"),
    path('clientes/', views.clientes, name="clientes"),
    path('notas/', views.notas, name="notas"),
    path('login/', views.login, name="login"),
    path('consulta/', views.consulta_produtos, name="consulta_produtos"),
    path('consultaClientes/', views.consulta_clientes, name="consulta_clientes"),
    path('inicioClientes/', views.inicio_clientes, name="inicio_clientes"),
    path('registroUsuarios', views.registro_usuario , name='registro_usuario'),
    path('emissaoNotas/', views.emissao_notas, name="emissao_notas"),
    path('selecaoCompra/', views.selecao_compra, name="selecao_compra"),

]

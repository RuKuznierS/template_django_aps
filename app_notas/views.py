from django.shortcuts import render
def home(request):
    return render(request, 'geral/index.html')

def produtos(request):
    return render(request, 'geral/produtos.html')

def clientes(request):
    return render(request, 'geral/clientes.html')

def notas(request):
    return render(request, 'geral/consulta_notas.html')

def login(request):
    return render(request, 'geral/login.html')

def consulta_produtos(request):
    return render(request, 'geral/consulta_produtos.html')

def consulta_clientes(request):
    return render(request, 'geral/consulta_clientes.html')

def inicio_clientes(request):
    return render(request, 'geral/principal_clientes.html')

def selecao_compra(request):
    return render(request, 'geral/selecao_compra.html')

def emissao_notas(request):
    return render(request, 'geral/emissaoNotas.html')

def registro_usuario(request):
    return render(request, 'geral/register.html')
from django.shortcuts import render
def home(request):
    return render(request, 'geral/index.html')

def produtos(request):
    return render(request, 'geral/produtos.html')

def clientes(request):
    return render(request, 'geral/clientes.html')

def notas(request):
    return render(request, 'geral/tables.html')

def login(request):
    return render(request, 'geral/login.html')
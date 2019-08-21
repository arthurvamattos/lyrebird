from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'index.html', context)


def resultados(request):
    context = {}
    return render(request, 'resultados.html', context)


def pedido_inclusao(request):
    context = {}
    return render(request, 'pedido_inclusao.html', context)

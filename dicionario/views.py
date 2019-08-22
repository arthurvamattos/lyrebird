from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models import Q
from .models import Termo, Sugestao
from .forms import TermoForm


def index(request):
    context = {}
    return render(request, 'index.html', context)


class ResultsView(ListView):
    model = Termo
    paginated_by = 20
    template_name = "resultados.html"

    def get_queryset(self):
        query = self.request.GET.get('q', '')

        new_context = {}
        try:
            new_context = Termo.objects.filter(
                Q(termo__icontains=query) | Q(expressao__icontains=query)
            )
        except Termo.DoesNotExist:
            new_context = {}

        return new_context


def resultados(request):
    context = {}
    return render(request, 'resultados.html', context)


def solicitacao_inclusao(request):
    print('SOLICITACAO INCLUSAO 1')
    context = {}
    form = TermoForm()
    if request.method == "POST":
        print('SOLICITACAO INCLUSAO 2')
        form = TermoForm(request.POST, request.FILES)
        if form.is_valid():
            print('SOLICITACAO INCLUSAO 3')
            termo = form.save(commit=False)
            termo.aprovado = False
            termo.save()
            sugestao = Sugestao()
            sugestao.usuario = request.user
            sugestao.termo = termo
            sugestao.save()
            context['saved'] = True
            context['form'] = TermoForm()
            return render(request, 'pedido_inclusao.html', context)

    else:
        print('SOLICITACAO INCLUSAO 4')

    context['form'] = form
    return render(request, 'pedido_inclusao.html', context)

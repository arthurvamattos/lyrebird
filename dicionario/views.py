from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from .models import Termo


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


def pedido_inclusao(request):
    context = {}
    return render(request, 'pedido_inclusao.html', context)

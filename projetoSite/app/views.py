from django.core import paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.

def listar_produto(request, categoria, template_name="produtos_list.html"):
    query = request.GET.get("busca", '')
    page = request.GET.get("page",'')
    ordenar = request.GET.get("ordenar",'')
    if query:
        if categoria != "todos":
            produto = Produto.objects.filter(nome__icontains=query, tipo=categoria)
        else:
            produto = Produto.objects.filter(nome__icontains=query)
    else:
        try:
            if categoria != "todos":
                if ordenar:
                    produto = Produto.objects.filter(tipo=categoria).order_by(ordenar)
                else:
                    produto = Produto.objects.filter(tipo=categoria)
            else:
                if ordenar:
                    produto = Produto.objects.all().order_by(ordenar)
                else:
                    produto = Produto.objects.all()
            produto = Paginator(produto,2)
            produto = produto.page(page)
        except PageNotAnInteger:
            produto = produto.page(1)
        except EmptyPage:
            produto = paginator.page(paginator.num_pages)
    produtos = {'lista': produto}
    return render(request, template_name, produtos)

def perfil_produto (request, pk, template_name="perfil_produto.html"):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, template_name, {'produto': produto})
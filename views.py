from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'webapp1/index.html'),

def pag2(r):
    dados = {'nome':'Agnaldo Silva', 'dade':50}

    return render(r, 'webapp1/pagina2.html', dados)
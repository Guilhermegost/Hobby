from django.shortcuts import render
from .models import Post

def pagina_inicial(request):
    # Busca todos os posts do banco de dados, do mais novo para o mais antigo
    posts = Post.objects.all().order_by('-data_criacao')
    # Envia os posts para o arquivo HTML que vamos criar
    return render(request, 'core/index.html', {'posts': posts})


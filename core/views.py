from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from .models import Post
from .forms import CadastroForm, PostForm

@require_http_methods(["GET", "POST"])
@login_required
def pagina_inicial(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.titulo = 'Publicação'
            post.autor = request.user
            post.save()
            messages.success(request, 'Sua publicação foi adicionada ao mural.')
            return redirect('home')
    else:
        form = PostForm()

    posts = Post.objects.all().order_by('-data_criacao')
    return render(request, 'core/index.html', {'posts': posts, 'form': form})

@require_http_methods(["GET", "POST"])
def pagina_cadastro(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CadastroForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')
    return render(request, 'core/cadastro.html', {'form': form})


@login_required
def pagina_configuracoes(request):
    return render(request, 'core/configuracoes.html')


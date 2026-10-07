from django.contrib import admin
from .models import Post

# Isso faz o formulário de Posts aparecer no painel administrativo
admin.site.register(Post)



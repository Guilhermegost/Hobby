"""
URL configuration for meu_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('entrar/', auth_views.LoginView.as_view(template_name='core/entrar.html', redirect_authenticated_user=True), name='entrar'),
    path('sair/', auth_views.LogoutView.as_view(), name='sair'),
    path('cadastro/', views.pagina_cadastro, name='cadastro'),
    path('', views.pagina_inicial, name='home'),
    path('configuracoes/', views.pagina_configuracoes, name='configuracoes'),
]

# Adiciona suporte para carregar as imagens do upload no modo de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

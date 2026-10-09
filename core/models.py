from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
    )
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    # Campo novo para a foto (opcional)
    imagem = models.ImageField(upload_to='post_fotos/', null=True, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo



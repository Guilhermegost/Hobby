from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['conteudo', 'imagem']
        labels = {'conteudo': '', 'imagem': 'Adicionar uma foto'}
        widgets = {
            'conteudo': forms.Textarea(attrs={
                'placeholder': 'No que você está pensando?',
                'rows': 3,
            }),
        }


class CadastroForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username',)

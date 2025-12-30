from django.urls import path
from . views import index, contato, produto, cadastro

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
    path('produto/cadastro/', cadastro, name='cadastrar_produto'),
]
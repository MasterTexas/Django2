from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca', 'preco', 'estoque', 'ativo', 'criado', 'modificado')
    search_fields = ('nome',)


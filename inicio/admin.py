from django.contrib import admin
from .models import Post


@admin.register(Post) # ADICIONA NO ADMIN
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'criado')
    search_fields = ('titulo', 'conteudo')
    list_filter = ('criado', 'autor')

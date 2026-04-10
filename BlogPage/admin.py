from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class PostAdmin(admin.ModelAdmin):

    # 1. Função dinâmica para esconder o campo
    def get_exclude(self, request, obj=None):
        # Se o usuário for um administrador master (superuser)
        if request.user.is_superuser:
            # Retorna None, ou seja, não esconde nada! Ele verá o campo 'autor'
            return []
        
        # Se for um usuário normal (staff), esconde o campo 'autor'
        return ['author']

    # 2. Intercepta o salvamento do painel Admin
    def save_model(self, request, obj, form, change):
        
        if not obj.author_id:
            obj.author = request.user
            
        super().save_model(request, obj, form, change)
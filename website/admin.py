from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'sub_titulo', 'categorias']
    search_fields = ['titulo', 'sub_titulo']

admin.site.register(Post, PostAdmin)
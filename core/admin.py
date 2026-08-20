from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'date_publication', 'publie')
    list_editable = ('publie',)
    prepopulated_fields = {'slug': ('titre',)}
    search_fields = ('titre', 'contenu')
    list_filter = ('publie', 'categorie')

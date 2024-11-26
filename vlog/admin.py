from django.contrib import admin
from .models import VlogPost

@admin.register(VlogPost)
class VlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'tags')
    list_filter = ('tags',)
    search_fields = ('title', 'author__username', 'tags') 
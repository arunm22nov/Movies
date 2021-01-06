
from django.contrib import admin
from .models import movies,genre

# Register your models here.

#admin.site.register(movies)

@admin.register(genre)
class AuthorAdmin2(admin.ModelAdmin):
    list_display=['genre_name']
    ordering = ['genre_name']

@admin.register(movies)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    fields = ('name', 'popularity','director','imdb_score','genre_m')
    list_display = ['name', 'popularity','director','imdb_score','get_genre']
    ordering = ['name']


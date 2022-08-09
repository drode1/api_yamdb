from django.contrib import admin
from .models import Category, Genre, Title


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'category', 'get_genres')
    search_fields = ('name',)
    list_filter = ('category', 'year')
    empty_value_display = '-пусто-'


admin.site.register(Title, TitleAdmin)
admin.site.register(Category)
admin.site.register(Genre)

from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    """ Класс для управления произведениями в админке. """

    list_display = ('pk', 'name', 'year', 'category', 'get_genres')
    search_fields = ('name',)
    list_filter = ('category', 'year')
    empty_value_display = '-пусто-'


admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Comment)

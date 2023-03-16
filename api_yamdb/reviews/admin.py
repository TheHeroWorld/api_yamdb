from django.contrib import admin
from .models import Title
from .models import Genre
from .models import Category



class TitlesAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'category',
        'description',
        'year'
    )
    filter_horizontal = ('genre',)


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
    )


admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitlesAdmin)
admin.site.register(Category, CategoryAdmin)


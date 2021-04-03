from django.contrib import admin

from .models import News, Category


# Отображение в админке название полей
class NewsAdmin(admin.ModelAdmin):
    # Акуратно, это все долбанные кортежи
    list_display = ('id', 'title', 'category','created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')  # Какие поля будут с ссылкой на объект
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    # Акуратно, это все долбанные кортежи
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

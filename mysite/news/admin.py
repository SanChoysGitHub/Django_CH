from django.contrib import admin

from .models import News


# Отображение в админке название полей
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')  # Какие поля будут с ссылкой на объект
    search_fields = ('title', 'content')


admin.site.register(News, NewsAdmin)




from django.shortcuts import render
from django.http.response import HttpResponse

from .models import News


def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': 'News list'
            }
    return render(request, template_name='news/index.html', context=context)


def test(request):
    return HttpResponse('<h1>Тестовая страница</h1>')


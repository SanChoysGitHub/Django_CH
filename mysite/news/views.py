from django.shortcuts import render, get_object_or_404, redirect

from .models import News, Category
from .forms import NewsForm

def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'News list',
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, template_name='news/category.html', context={'news': news, 'category': category})


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})


def add_news(request):
    if request.method == 'POST':  # Проверка метода
        form = NewsForm(request.POST)  # Заполнение данными которые пришли в форму
        if form.is_valid():  # Прошло ли значение валидацию
            # print(form.cleaned_data)
            # news = News.objects.create(**form.cleaned_data)  # Сохранение очищенных данных
            news = form.save()  # Сохранение данных
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', context={'form': form})


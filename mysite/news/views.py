from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import News, Category
from .forms import NewsForm


# Получение списка объектов для какой либо странице
class HomeView(ListView):
    model = News  # Получение данных News
    template_name = 'news/home_news_list.html'  # Переопределение шаблона
    context_object_name = 'news'  # Переопределение названия объекта
    # extra_context = {'title': 'Home'}  # Для стат данных

    # Для динамических данных(Переопределяем метод)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # *Возращение родительского метода
        context['title'] = 'Home page'   # Добавление шапки сайта
        return context

    # Вывод контента который ОПУБЛИКОВАН
    def get_queryset(self):
        return News.objects.filter(is_published=True)


# Вывод категорий
class NewsByCategory(ListView):
    model = News  # Получение данных News
    template_name = 'news/home_news_list.html'  # Переопределение шаблона
    context_object_name = 'news'  # Переопределение названия объекта
    allow_empty = False  # Запрет на показ не найденных или не опубл. списков(контента)

    # Для динамических данных(Переопределяем метод)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # *Возращение родительского метода
        # Изменение шапки страницы на выбранную категорию
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    # Вывод контента который ОПУБЛИКОВАН(Переопределяем метод)
    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


# Вывод информации единичного контента
class ViewNews(DetailView):
    model = News  # Модель с которой мы работаем
    context_object_name = 'news_item'  # Переопределение переменной
    # template_name = 'news/news_detail.html'  # Переопределение шаблона
    # pk_url_kwarg = 'news_id'  # Переопределение переменной индетификации


# Сохранение формы
class CreateNews(CreateView):
    form_class = NewsForm  # Связывание с формой
    template_name = 'news/add_news.html'  # Переопределение шаблона
    # success_url = reverse_lazy('home')  #  Переход на страницу


# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'News list',
#     }
#     return render(request, template_name='news/index.html', context=context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, template_name='news/category.html', context={'news': news, 'category': category})


# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {"news_item": news_item})


# def add_news(request):
#     if request.method == 'POST':  # Проверка метода
#         form = NewsForm(request.POST)  # Заполнение данными которые пришли в форму
#         if form.is_valid():  # Прошло ли значение валидацию
#             # news = News.objects.create(**form.cleaned_data)  # Сохранение очищенных данных
#             news = form.save()  # Сохранение данных
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', context={'form': form})



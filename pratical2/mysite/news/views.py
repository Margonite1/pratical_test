from django.shortcuts import render

from django.http import HttpResponse

from .models import News_Item


def index(request):
    news_list = News_Item.objects.all
    context_dict = {'News_items' : news_list}
    return render(request, 'news/news.html', context=context_dict)
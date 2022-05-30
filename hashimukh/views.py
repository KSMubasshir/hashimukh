from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic.edit import CreateView
from .models import News


def index(request):
    template = loader.get_template('home/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def contact(request):
    template = loader.get_template('contacts/contact.html')
    context = {}
    return HttpResponse(template.render(context, request))


def news(request):
    all_news_list = News.objects.all()
    context = {'all_news_list': all_news_list}
    return render(request, 'news/news.html', context)

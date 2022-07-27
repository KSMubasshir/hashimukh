from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic.edit import CreateView
from .models import News, Project


def index(request):
    template = loader.get_template('home/index.html')
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    context = {
        'all_news_list': all_news_list,
        'all_project_list': all_project_list
    }
    return HttpResponse(template.render(context, request))


def contact(request):
    template = loader.get_template('contacts/contact.html')
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    context = {
        'all_news_list': all_news_list,
        'all_project_list': all_project_list
    }
    return HttpResponse(template.render(context, request))


def news(request, news_id):
    news = News.objects.get(news_id=news_id)
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    context = {
        'news': news,
        'all_news_list': all_news_list,
        'all_project_list': all_project_list
    }
    return render(request, 'news/news.html', context)


def project(request, project_id):
    project = Project.objects.get(project_id=project_id)
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    context = {
        'project': project,
        'all_news_list': all_news_list,
        'all_project_list': all_project_list
    }
    return render(request, 'projects/project.html', context)


def donate(request):
    template = loader.get_template('donation/donate.html')
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    context = {
        'all_news_list': all_news_list,
        'all_project_list': all_project_list
    }
    return HttpResponse(template.render(context, request))


def joinus(request):
    template = loader.get_template('joinus/joinus.html')
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    context = {
        'all_news_list': all_news_list,
        'all_project_list': all_project_list
    }
    return HttpResponse(template.render(context, request))

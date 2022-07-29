from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic.edit import CreateView
from .models import News, Project, Focus, FocussedProject


def index(request):
    template = loader.get_template('home/index.html')
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    all_focus_list = Focus.objects.all()
    context = {
        'all_news_list': all_news_list,
        'all_project_list': all_project_list,
        'all_focus_list': all_focus_list
    }
    return HttpResponse(template.render(context, request))


def contact(request):
    template = loader.get_template('contacts/contact.html')
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    all_focus_list = Focus.objects.all()
    context = {
        'all_news_list': all_news_list,
        'all_project_list': all_project_list,
        'all_focus_list': all_focus_list
    }
    return HttpResponse(template.render(context, request))


def news(request, news_id):
    news = News.objects.get(news_id=news_id)
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    all_focus_list = Focus.objects.all()
    context = {
        'news': news,
        'all_news_list': all_news_list,
        'all_project_list': all_project_list,
        'all_focus_list': all_focus_list
    }
    return render(request, 'news/news.html', context)


def project(request, project_id):
    project = Project.objects.get(project_id=project_id)
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    all_focus_list = Focus.objects.all()
    context = {
        'project': project,
        'all_news_list': all_news_list,
        'all_project_list': all_project_list,
        'all_focus_list': all_focus_list
    }
    return render(request, 'projects/project.html', context)


def donate(request):
    template = loader.get_template('donation/donate.html')
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    all_focus_list = Focus.objects.all()
    context = {
        'all_news_list': all_news_list,
        'all_project_list': all_project_list,
        'all_focus_list': all_focus_list
    }
    return HttpResponse(template.render(context, request))


def joinus(request):
    template = loader.get_template('joinus/joinus.html')
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    all_focus_list = Focus.objects.all()
    context = {
        'all_news_list': all_news_list,
        'all_project_list': all_project_list,
        'all_focus_list': all_focus_list
    }
    return HttpResponse(template.render(context, request))


def focus(request, focus_id):
    focus = Focus.objects.get(focus_id=focus_id)
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    focussed_projects = FocussedProject.objects.filter(focus_id=focus_id)
    all_focus_list = Focus.objects.all()
    context = {
        'focus': focus,
        'all_news_list': all_news_list,
        'all_project_list': all_project_list,
        'focussed_projects': focussed_projects,
        'all_focus_list': all_focus_list
    }
    return render(request, 'focus/focus.html', context)
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic.edit import CreateView
from .models import News, Project, Focus, FocussedProject, EventsLevelOne, EventsLevelTwo


def index(request):
    template = loader.get_template('home/index.html')
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    all_focus_list = Focus.objects.all()
    events_level_one_list = EventsLevelOne.objects.all()
    events = []
    for event_level_one in events_level_one_list:
        event = {}
        event['event_level_one'] = event_level_one
        event['events_level_two'] = EventsLevelTwo.objects.filter(event_level_one_id_id=event_level_one.event_level_one_id)
        events.append(event)
    context = {
        'all_news_list': all_news_list,
        'all_project_list': all_project_list,
        'all_focus_list': all_focus_list,
        'events': events
    }
    return HttpResponse(template.render(context, request))


def contact(request):
    template = loader.get_template('contacts/contact.html')
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    all_focus_list = Focus.objects.all()
    events_level_one_list = EventsLevelOne.objects.all()
    events = []
    for event_level_one in events_level_one_list:
        event = {}
        event['event_level_one'] = event_level_one
        event['events_level_two'] = EventsLevelTwo.objects.filter(
            event_level_one_id_id=event_level_one.event_level_one_id)
        events.append(event)
    context = {
        'all_news_list': all_news_list,
        'all_project_list': all_project_list,
        'all_focus_list': all_focus_list,
        'events': events
    }
    return HttpResponse(template.render(context, request))


def news(request, news_id):
    news = News.objects.get(news_id=news_id)
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    all_focus_list = Focus.objects.all()

    events_level_one_list = EventsLevelOne.objects.all()
    events = []
    for event_level_one in events_level_one_list:
        event = {}
        event['event_level_one'] = event_level_one
        event['events_level_two'] = EventsLevelTwo.objects.filter(
            event_level_one_id_id=event_level_one.event_level_one_id)
        events.append(event)
    context = {
        'news': news,
        'all_news_list': all_news_list,
        'all_project_list': all_project_list,
        'all_focus_list': all_focus_list,
        'events': events
    }
    return render(request, 'news/news.html', context)


def project(request, project_id):
    project = Project.objects.get(project_id=project_id)
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    all_focus_list = Focus.objects.all()

    events_level_one_list = EventsLevelOne.objects.all()
    events = []
    for event_level_one in events_level_one_list:
        event = {}
        event['event_level_one'] = event_level_one
        event['events_level_two'] = EventsLevelTwo.objects.filter(
            event_level_one_id_id=event_level_one.event_level_one_id)
        events.append(event)
    context = {
        'project': project,
        'all_news_list': all_news_list,
        'all_project_list': all_project_list,
        'all_focus_list': all_focus_list,
        'events': events
    }
    return render(request, 'projects/project.html', context)


def donate(request):
    template = loader.get_template('donation/donate.html')
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    all_focus_list = Focus.objects.all()

    events_level_one_list = EventsLevelOne.objects.all()
    events = []
    for event_level_one in events_level_one_list:
        event = {}
        event['event_level_one'] = event_level_one
        event['events_level_two'] = EventsLevelTwo.objects.filter(
            event_level_one_id_id=event_level_one.event_level_one_id)
        events.append(event)
    context = {
        'all_news_list': all_news_list,
        'all_project_list': all_project_list,
        'all_focus_list': all_focus_list,
        'events': events
    }
    return HttpResponse(template.render(context, request))


def joinus(request):
    template = loader.get_template('joinus/joinus.html')
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    all_focus_list = Focus.objects.all()

    events_level_one_list = EventsLevelOne.objects.all()
    events = []
    for event_level_one in events_level_one_list:
        event = {}
        event['event_level_one'] = event_level_one
        event['events_level_two'] = EventsLevelTwo.objects.filter(
            event_level_one_id_id=event_level_one.event_level_one_id)
        events.append(event)
    context = {
        'all_news_list': all_news_list,
        'all_project_list': all_project_list,
        'all_focus_list': all_focus_list,
        'events': events
    }
    return HttpResponse(template.render(context, request))


def focus(request, focus_id):
    focus = Focus.objects.get(focus_id=focus_id)
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    focussed_projects = FocussedProject.objects.filter(focus_id=focus_id)
    all_focus_list = Focus.objects.all()
    events_level_one_list = EventsLevelOne.objects.all()
    events = []
    for event_level_one in events_level_one_list:
        event = {}
        event['event_level_one'] = event_level_one
        event['events_level_two'] = EventsLevelTwo.objects.filter(
            event_level_one_id_id=event_level_one.event_level_one_id)
        events.append(event)
    context = {
        'focus': focus,
        'all_news_list': all_news_list,
        'all_project_list': all_project_list,
        'focussed_projects': focussed_projects,
        'all_focus_list': all_focus_list,
        'events': events
    }
    return render(request, 'focus/focus.html', context)


def event(request, event_level_one_id):
    event_level_one = EventsLevelOne.objects.get(event_level_one_id=event_level_one_id)
    all_news_list = News.objects.all()
    all_project_list = Project.objects.all()
    all_focus_list = Focus.objects.all()

    events_level_one_list = EventsLevelOne.objects.all()
    events = []
    for event_level_one in events_level_one_list:
        event = {}
        event['event_level_one'] = event_level_one
        event['events_level_two'] = EventsLevelTwo.objects.filter(
            event_level_one_id_id=event_level_one.event_level_one_id)
        events.append(event)
    context = {
        'event_level_one': event_level_one,
        'all_news_list': all_news_list,
        'all_project_list': all_project_list,
        'all_focus_list': all_focus_list,
        'events': events
    }
    return render(request, 'event/event.html', context)

from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('home/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def contact(request):
    template = loader.get_template('contacts/contact.html')
    context = {}
    return HttpResponse(template.render(context, request))

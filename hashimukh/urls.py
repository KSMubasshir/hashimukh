from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('donate/', views.donate, name='donate'),
    path('joinus/', views.joinus, name='joinus'),
    path('admin/', admin.site.urls, name='admin'),
    path('news/<int:news_id>', views.news, name='news'),
    path('projects/<int:project_id>', views.project, name='project'),
    path('focus/<int:focus_id>', views.focus, name='focus'),
    path('event/<int:event_level_one_id>', views.event, name='event')
]

# add this line to link the static files in the url
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

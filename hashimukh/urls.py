from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls, name='admin'),
    path('news/', views.news, name='news'),
]

# add this line to link the static files in the url
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
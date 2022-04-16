from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('hashimukh/', include('hashimukh.urls')),
    path('admin/', admin.site.urls),
]
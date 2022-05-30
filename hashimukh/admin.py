from django.contrib import admin

# Register your models here.
from .models import News

admin.site.register(News)


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('news_publish_date', 'news_title')

    # list_editable = ['actual_problem']

    list_filter = (
        'news_publish_date',
    )

    list_per_page = 10
    list_display = (
        'news_publish_date',
        'news_image',
        'news_title',
        'news_content')

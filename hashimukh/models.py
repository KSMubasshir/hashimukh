from django.db import models


# Create your models here.

class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    news_publish_date = models.DateField()
    news_image = models.ImageField(upload_to='images')
    news_title = models.TextField()
    news_content = models.TextField()

    def __str__(self):
        return self.news_title


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_title = models.TextField()
    project_publish_date = models.DateField()
    project_image = models.ImageField(upload_to='images')
    project_tagline = models.TextField()
    project_content = models.TextField()

    def __str__(self):
        return self.project_title


class Focus(models.Model):
    focus_id = models.AutoField(primary_key=True)
    focus_title = models.TextField()
    focus_image = models.ImageField(upload_to='images')
    focus_icon = models.ImageField(upload_to='images', default="")

    def __str__(self):
        return self.focus_title

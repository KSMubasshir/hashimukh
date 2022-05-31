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

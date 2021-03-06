import datetime as dt
from django.db import models

# Create your models here.


class Editor(models.Model):
    """
    Editor model class
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

    def delete_editor(self):
        self.delete()

    class Meta:
        ordering = ['first_name']


class tags(models.Model):
    """
    Tags model class
    """
    name = models.CharField(max_length=200, default='testing')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/',default = 'image.jpg')

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date=today)

        return news

    @classmethod
    def date_news(cls, date):
        news = cls.objects.filter(pub_date__date=date)

        return news

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news

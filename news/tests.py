import datetime as dt
from django.test import TestCase
from .models import Editor, Article, tags

# Create your tests here.


class EditorTestClass(TestCase):
    """
    Test class for the editor model class
    """

    def setUp(self):
        """
        Creates instance of Editor module before each test
        """
        self.denis = Editor(first_name='Denis',
                            last_name='Kibet', email='kibet@gmail.com')

    def test_instance(self):
        """
        Test method to check for correct instantiation
        """
        self.assertTrue(isinstance(self.denis, Editor))

    def test_save_method(self):
        self.denis.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    def test_delete_method(self):
        self.denis.save_editor()
        self.denis.delete_editor()
        noeditors = Editor.objects.all()
        self.assertTrue(len(noeditors) == 0)


class ArticleTestClass(TestCase):
    """
    Test class for the Article module
    """

    def setUp(self):
        """
        """
        self.rule = Editor(first_name='Ja', last_name='Rule',
                           email='ja@rule.com')
        self.rule.save_editor()

        self.new_tag = tags(name='testing')
        self.new_tag.save()

        self.new_article = Article(
            title='Test Article', post='This is a random test Post', editor=self.rule)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)

    def test_get_news_by_date(self):
        test_date = '2019-07-16'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.date_news(date)
        self.assertTrue(len(news_by_date) > 0)
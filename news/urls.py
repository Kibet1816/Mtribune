from django.conf.urls import url
from . import views

# Urlpatterns:List of url instances for our app
urlpatterns=[
    url('^$',views.news_of_day,name='newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name='pastNews')
]
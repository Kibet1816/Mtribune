from django.conf.urls import url
from . import views

# Urlpatterns:List of url instances for our app
urlpatterns=[
    url('^$',views.welcome,name='welcome'),
    url('^today/$',views.news_of_day,name='newsToday')
]
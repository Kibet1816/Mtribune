import datetime as dt
from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import Article

# Create your views here.


def welcome(request):
    """
    View function to render the welcome page

    Args:
        Request:Contains info of the current web request that has triggered hte view
    """
    return render(request,'welcome.html')


def news_of_day(request):
    """
    View function responsible for returning news fro specific day
    """
    date = dt.date.today()
    news = Article.todays_news()
    return render(request, 'all-news/today-news.html',{"date":date,"news":news})


def convert_dates(dates):
    """
    Function that gets the weekday number for the date
    """
    day_number = dt.date.weekday(dates)

    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']

    day = days[day_number]
    return day


def past_days_news(request, past_date):
    """
    Function that converts data from the string url
    """
    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    news = Article.date_news(date)
    return render(request,'all-news/past-news.html',{"date":date,"news":news})

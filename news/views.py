import datetime as dt
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def welcome(request):
    """
    View function to render the welcome page

    Args:
        Request:Contains info of the current web request that has triggered hte view
    """
    return HttpResponse('Welcome to the Moringa Tribune')

def news_of_day(request):
    """
    View function responsible for returning news fro specific day
    """
    date = dt.date.today()
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1> News for {day} {date.day}-{date.month}-{date.year} </h1>
            </body>
        </html>
    '''
    return HttpResponse(html)

def convert_dates(dates):
    """
    Function that gets the weekday number for the date
    """
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    day = days[day_number]
    return day
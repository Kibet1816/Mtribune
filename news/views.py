from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def welcome(request):
    """
    View function to render the welcome page

    Args:
        Request:Contains info of the current web request that has triggered hte view
    """
    return HttpResponse('Welcome to the Moringa Tribune')

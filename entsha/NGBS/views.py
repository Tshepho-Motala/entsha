from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from datetime import datetime

from django.shortcuts import render

# Create your views here.

def NGBS(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'NGBS/index.html',
        {
            'title':'NGBS',
            'message':'Welcome to NGBS page',
            'year':datetime.now().year,
        }
    )


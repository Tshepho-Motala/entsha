from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from datetime import datetime

from django.shortcuts import render

# Create your views here.

def NGMC(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'NGMC/index.html',
        {
            'title':'NGMC',
            'message':'Welcome to NGMC page',
            'year':datetime.now().year,
        }
    )

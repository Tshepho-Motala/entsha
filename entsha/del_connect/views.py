from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from datetime import datetime

from django.shortcuts import render

# Create your views here.

def DelConnect(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'del_connect/index.html',
        {
            'title':'Del Connect',
            'message':'Welcome to Del Connect page',
            'year':datetime.now().year,
        }
    )

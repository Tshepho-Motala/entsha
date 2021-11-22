from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from .models import *
from .forms import LeadForm, DelphiusEmployeeForm, interest_Form
from datetime import datetime

# Create your views here.

def delphius_home(request):
    """Renders the delphius page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'delphius/index.html',
        {
            'title':'delphius Page',
            'year':datetime.now().year,
        }
    )

def delphius_list(request):
    return render(request, "delphius/employee_list.html")

def delphius_form(request):
    if request.method == "GET":
        form = DelphiusEmployeeForm()
        return render(request, "delphius/employee_form.html", {'form':form})
    else:
        form = DelphiusEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/delphius/list')

def delphius_delete(request):
    return


def lead_list(request):
    context = {'lead_list':Lead.objects.all()}
    return render(request, "delphius/lead_list.html", context)

def lead_form(request, id=0):
    if request.method == "GET":
        form = LeadForm()
        return render(request, "delphius/lead_form.html", {'form':form})
    else:
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/delphius/lead_list')

def lead_delete(request, id):
    lead = Lead.objects.get(pk=id)
    lead.delete()
    return redirect('/delphius/lead_list')

def interest_list(request):
    context = {'interest_list':Delphius_interest.objects.all()}
    return render(request, "delphius/interest_list.html", context)

def interest_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
           form = interest_Form()
        else:
            interest = Delphius_interest.objects.get(pk=id)
            form = Delphius_interest_Form(instance=interest)
        return render(request, "delphius/interest_form.html", {'form': form})
    else:
       form = Delphius_interest_Form(request.POST)
       if form.is_valid():
           form.save()
       return redirect('/delphius/interest_list')

def interest_delete(request, id):
    delphius_interest = Delphius_interest.objects.get(pk=id)
    Delphius_interest.delete()
    return redirect('/delphius/interest_list')